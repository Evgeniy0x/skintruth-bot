"""
╔═══════════════════════════════════════════════╗
║  SkinTruth — AI-Анализатор Косметики v2.0     ║
║  Бесплатный AI через OpenRouter               ║
║  Telegram: @Cosmoceftbot                      ║
╚═══════════════════════════════════════════════╝
"""

import os
import re
import json
import base64
import logging
import sqlite3
import asyncio
from datetime import datetime
from pathlib import Path

import httpx
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import (
    Update, InlineKeyboardButton, InlineKeyboardMarkup,
    ReplyKeyboardMarkup, KeyboardButton, BotCommand
)
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    CallbackQueryHandler, ContextTypes, filters, ConversationHandler
)
from telegram.constants import ParseMode, ChatAction

# ═══════════════ НАСТРОЙКИ ═══════════════

BOT_TOKEN = "8770083271:AAFP1-5WXuhdLPCBHu81XyxzAhPbVG_Jd8s"
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
PORT = int(os.environ.get("PORT", 10000))

# Бесплатные модели OpenRouter
AI_MODEL_TEXT = "meta-llama/llama-3.3-70b-instruct:free"      # 70B — умный для текста
AI_MODEL_VISION = "google/gemma-3-27b-it:free"                 # 27B — с Vision для фото
AI_MODEL_FALLBACK = "mistralai/mistral-small-3.1-24b-instruct:free"  # запасной

BOT_VERSION = "2.0"
MAX_ANALYSES_FREE = 50  # бесплатных анализов в день на юзера
DB_PATH = Path(__file__).parent / "skintruth.db"

# ═══════════════ ЛОГГИРОВАНИЕ ═══════════════

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    level=logging.INFO
)
logger = logging.getLogger("SkinTruth")

# ═══════════════ БАЗА ДАННЫХ ═══════════════

def init_db():
    """Создать таблицы если не существуют."""
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            skin_type TEXT DEFAULT '',
            analyses_count INTEGER DEFAULT 0,
            joined_at TEXT DEFAULT CURRENT_TIMESTAMP,
            last_active TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            input_type TEXT,
            input_text TEXT,
            result TEXT,
            score INTEGER,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_user(user):
    """Сохранить/обновить юзера."""
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    c.execute("""
        INSERT INTO users (user_id, username, first_name, last_active)
        VALUES (?, ?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT(user_id) DO UPDATE SET
            username=excluded.username,
            first_name=excluded.first_name,
            last_active=CURRENT_TIMESTAMP
    """, (user.id, user.username or "", user.first_name or ""))
    conn.commit()
    conn.close()

def get_user_skin_type(user_id):
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    c.execute("SELECT skin_type FROM users WHERE user_id=?", (user_id,))
    row = c.fetchone()
    conn.close()
    return row[0] if row and row[0] else None

def set_user_skin_type(user_id, skin_type):
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    c.execute("UPDATE users SET skin_type=? WHERE user_id=?", (skin_type, user_id))
    conn.commit()
    conn.close()

def increment_analyses(user_id):
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    c.execute("UPDATE users SET analyses_count = analyses_count + 1 WHERE user_id=?", (user_id,))
    conn.commit()
    conn.close()

def save_analysis(user_id, input_type, input_text, result, score=0):
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    c.execute("""
        INSERT INTO analyses (user_id, input_type, input_text, result, score)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, input_type, input_text[:500], result[:4000], score))
    conn.commit()
    conn.close()

def get_user_history(user_id, limit=5):
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    c.execute("""
        SELECT input_type, input_text, score, created_at
        FROM analyses WHERE user_id=?
        ORDER BY created_at DESC LIMIT ?
    """, (user_id, limit))
    rows = c.fetchall()
    conn.close()
    return rows

def get_stats():
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM users")
    users = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM analyses")
    analyses = c.fetchone()[0]
    conn.close()
    return users, analyses

# ═══════════════ ТИПЫ КОЖИ ═══════════════

SKIN_TYPES = {
    "normal": {"emoji": "😊", "name": "Нормальная", "desc": "Сбалансированная, без проблем"},
    "dry": {"emoji": "🏜️", "name": "Сухая", "desc": "Стянутость, шелушение"},
    "oily": {"emoji": "💧", "name": "Жирная", "desc": "Блеск, расширенные поры"},
    "combination": {"emoji": "🔄", "name": "Комбинированная", "desc": "T-зона жирная, щёки сухие"},
    "sensitive": {"emoji": "🌸", "name": "Чувствительная", "desc": "Реакции, покраснения"},
}

# ═══════════════ AI ПРОМТЫ ═══════════════

SYSTEM_PROMPT = """Ты — SkinTruth, профессиональный AI-косметолог и эксперт по косметической химии с 15-летним опытом.

Ты получаешь состав (INCI) косметического продукта. Проведи ГЛУБОКИЙ ЭКСПЕРТНЫЙ анализ.

ПРАВИЛА ОТВЕТА:
1. Используй ТОЛЬКО HTML-теги: <b>, <i>, <code> (НЕ markdown!)
2. Максимум 3500 символов
3. Отвечай ТОЛЬКО на русском языке
4. Будь конкретным — называй точные цифры, факты
5. Себестоимость считай в рублях (₽)

ФОРМАТ ОТВЕТА (строго следуй):

🔬 <b>SkinTruth • Экспертный анализ</b>

📊 <b>Оценка безопасности: XX/100</b> [5 кружков: 🟢🟢🟢🟡🔴]
(используй 🟢 для безопасных позиций, 🟡 для средних, 🔴 для опасных — всего 5)

📋 Найдено ингредиентов: XX

┌─────────────────────────┐
│ ✅ <b>Безопасные</b> (XX)       │
├─────────────────────────┤
│ перечисли через запятую  │
└─────────────────────────┘

┌─────────────────────────┐
│ ⚠️ <b>Спорные</b> (XX)          │
├─────────────────────────┤
│ перечисли через запятую  │
└─────────────────────────┘

┌─────────────────────────┐
│ 🔴 <b>Опасные</b> (XX)          │
├─────────────────────────┤
│ перечисли через запятую  │
└─────────────────────────┘

💰 <b>Реальная себестоимость</b>
💵 Ингредиенты: ~XX-XX ₽ / банка 50мл
🏷️ Розничная цена: обычно XX-XX ₽
📈 Наценка бренда: ~XXXX%

🧪 <b>Топ-5 ключевых ингредиентов</b>

1. <b>Название</b> (русское) — [✅|⚠️|🔴] X/10
   ↳ что делает и почему важен

2. ...

⚠️ <b>На что обратить внимание</b>
[аллергены, комедогенность, несовместимости]

{SKIN_CONTEXT}

📋 <b>Вердикт</b>
[рекомендация: кому подходит, кому нет, стоит ли покупать, на что заменить]

<i>SkinTruth v2.0 • AI-анализ</i>"""

SYSTEM_PROMPT_PHOTO = """Ты — SkinTruth, профессиональный AI-косметолог.

На фото — этикетка или упаковка косметического продукта.

ЗАДАЧА:
1. Определи что на фото: состав (Ingredients/INCI), описание, предупреждения, лицевая сторона
2. Если видишь СОСТАВ — распознай ВСЕ ингредиенты и проведи полный анализ
3. Если НЕТ состава — опиши что видишь и попроси фото с составом
4. Если фото нечёткое — скажи об этом

Если нашёл состав, используй тот же формат анализа что и для текста (HTML-теги, оценка/100, разбор ингредиентов, себестоимость, вердикт).

Если НЕ нашёл состав, ответь:

📸 <b>Фото получено</b>

На фото я вижу: [описание — что на фото]

❌ <b>Состав (Ingredients) не найден</b>

Пожалуйста, сфотографируй обратную сторону упаковки, где написан <b>состав</b> (обычно мелким шрифтом, начинается со слова Ingredients или Состав).

💡 <i>Совет: фотографируй при хорошем освещении, держи камеру ровно</i>

ПРАВИЛА: HTML-теги (<b>, <i>, <code>), НЕ markdown. Максимум 3500 символов. Только русский язык.
{SKIN_CONTEXT}"""


def get_skin_context(user_id):
    """Получить контекст типа кожи для промта."""
    skin = get_user_skin_type(user_id)
    if skin and skin in SKIN_TYPES:
        st = SKIN_TYPES[skin]
        return f"\n\n🧴 <b>Для вашей кожи ({st['name'].lower()})</b>\n[дай персональную рекомендацию для {st['name'].lower()} кожи: подходит ли этот состав, на что обратить внимание]"
    return ""


# ═══════════════ OPENROUTER API ═══════════════

async def call_openrouter(messages, model=None, timeout=90):
    """Универсальный вызов OpenRouter API."""
    if not OPENROUTER_API_KEY:
        return None

    model = model or AI_MODEL_TEXT

    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://t.me/Cosmoceftbot",
                    "X-Title": "SkinTruth Bot v2",
                },
                json={
                    "model": model,
                    "max_tokens": 2500,
                    "temperature": 0.3,
                    "messages": messages,
                }
            )

            if response.status_code == 200:
                data = response.json()
                content = data["choices"][0]["message"]["content"]
                logger.info(f"AI ответ ({model}): {len(content)} символов")
                return content
            else:
                logger.error(f"OpenRouter [{model}] {response.status_code}: {response.text[:200]}")
                return None
    except Exception as e:
        logger.error(f"OpenRouter [{model}] ошибка: {e}")
        return None


async def ai_analyze_text(text, user_id):
    """AI-анализ текстового состава."""
    skin_ctx = get_skin_context(user_id)
    prompt = SYSTEM_PROMPT.replace("{SKIN_CONTEXT}", skin_ctx)

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": f"Проанализируй состав:\n\n{text}"}
    ]

    # Пробуем основную модель
    result = await call_openrouter(messages, AI_MODEL_TEXT)
    if result:
        return result

    # Фоллбэк
    result = await call_openrouter(messages, AI_MODEL_FALLBACK)
    return result


async def ai_analyze_photo(image_bytes, user_id):
    """AI-анализ фото через Vision."""
    skin_ctx = get_skin_context(user_id)
    prompt = SYSTEM_PROMPT_PHOTO.replace("{SKIN_CONTEXT}", skin_ctx)
    b64 = base64.b64encode(image_bytes).decode('utf-8')

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": [
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}},
            {"type": "text", "text": "Проанализируй эту этикетку/упаковку косметики."}
        ]}
    ]

    result = await call_openrouter(messages, AI_MODEL_VISION, timeout=120)
    return result


# ═══════════════ КЛАВИАТУРЫ ═══════════════

def main_keyboard():
    """Постоянная клавиатура внизу экрана."""
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton("📸 Анализ фото"), KeyboardButton("✍️ Анализ текста")],
            [KeyboardButton("🧴 Мой тип кожи"), KeyboardButton("📊 История")],
            [KeyboardButton("ℹ️ О боте")],
        ],
        resize_keyboard=True,
        input_field_placeholder="Отправь состав или фото..."
    )


def skin_type_keyboard():
    """Выбор типа кожи."""
    buttons = []
    for key, val in SKIN_TYPES.items():
        buttons.append([InlineKeyboardButton(
            f"{val['emoji']} {val['name']} — {val['desc']}",
            callback_data=f"skin_{key}"
        )])
    buttons.append([InlineKeyboardButton("❌ Пропустить", callback_data="skin_skip")])
    return InlineKeyboardMarkup(buttons)


def after_analysis_keyboard():
    """Кнопки после анализа."""
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🔬 Новый анализ", callback_data="new_analysis"),
            InlineKeyboardButton("📊 История", callback_data="show_history"),
        ],
        [
            InlineKeyboardButton("💡 Подобрать аналог", callback_data="find_analog"),
            InlineKeyboardButton("📤 Поделиться", switch_inline_query=""),
        ],
    ])


def welcome_keyboard():
    """Кнопки на приветственном экране."""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔬 Начать анализ", callback_data="new_analysis")],
        [InlineKeyboardButton("🧴 Указать тип кожи", callback_data="choose_skin")],
        [InlineKeyboardButton("❓ Как пользоваться", callback_data="how_to")],
    ])


# ═══════════════ ОБРАБОТЧИКИ ═══════════════

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Приветствие — красивый welcome screen."""
    user = update.effective_user
    save_user(user)
    logger.info(f"/start от {user.id} ({user.first_name})")

    users_count, analyses_count = get_stats()
    skin = get_user_skin_type(user.id)
    skin_info = f"🧴 Ваш тип кожи: <b>{SKIN_TYPES[skin]['name']}</b>" if skin and skin in SKIN_TYPES else "🧴 Тип кожи: <i>не указан</i>"

    text = (
        f"╔══════════════════════════╗\n"
        f"║   🔬 <b>SkinTruth</b> v{BOT_VERSION}        ║\n"
        f"║   AI-Анализатор Косметики   ║\n"
        f"╚══════════════════════════╝\n\n"
        f"Привет, <b>{user.first_name}</b>! 👋\n\n"
        f"Я разберу состав <b>любого</b> косметического средства и расскажу:\n\n"
        f"  🧪 Что делает <b>каждый ингредиент</b>\n"
        f"  ⚠️ Какие компоненты <b>опасны</b>\n"
        f"  💰 Сколько <b>реально стоит</b> продукт\n"
        f"  🎯 <b>Персональную рекомендацию</b> для вашей кожи\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"{skin_info}\n"
        f"👥 Пользователей: <b>{users_count}</b>\n"
        f"🔬 Анализов: <b>{analyses_count}</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"<b>Отправь мне:</b>\n"
        f"📸 <b>Фото</b> этикетки с составом\n"
        f"✍️ <b>Текст</b> состава (скопируй с сайта)\n"
    )

    await update.message.reply_text(
        text, parse_mode=ParseMode.HTML,
        reply_markup=main_keyboard()
    )
    await update.message.reply_text(
        "👇 Выбери действие:",
        parse_mode=ParseMode.HTML,
        reply_markup=welcome_keyboard()
    )


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Подробная справка."""
    text = (
        "❓ <b>Как пользоваться SkinTruth</b>\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "<b>Способ 1: Фото 📸</b>\n"
        "Сфотографируй этикетку с составом (Ingredients).\n"
        "AI прочитает и проанализирует все ингредиенты.\n\n"
        "<b>Способ 2: Текст ✍️</b>\n"
        "Скопируй состав с сайта магазина или с упаковки.\n"
        "Просто вставь текст — бот поймёт.\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "<b>Что ты получишь:</b>\n\n"
        "📊 <b>Оценка безопасности</b> 0-100 баллов\n"
        "🧪 <b>Разбор каждого ингредиента</b> с рейтингом\n"
        "💰 <b>Реальная себестоимость</b> vs цена в магазине\n"
        "⚠️ <b>Предупреждения</b> об опасных компонентах\n"
        "🧴 <b>Персональные советы</b> для вашего типа кожи\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "💡 <b>Совет:</b> Укажи свой тип кожи (кнопка 🧴) —\n"
        "анализ станет персональным!"
    )
    await update.message.reply_text(text, parse_mode=ParseMode.HTML)


async def handle_menu_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка кнопок постоянной клавиатуры."""
    text = update.message.text
    user_id = update.effective_user.id

    if text == "📸 Анализ фото":
        await update.message.reply_text(
            "📸 <b>Анализ по фото</b>\n\n"
            "Отправь фото этикетки с составом.\n\n"
            "💡 <i>Совет: фотографируй при хорошем свете, "
            "держи камеру ровно, чтобы текст был чётким</i>",
            parse_mode=ParseMode.HTML
        )
    elif text == "✍️ Анализ текста":
        await update.message.reply_text(
            "✍️ <b>Анализ по тексту</b>\n\n"
            "Скопируй состав с упаковки или сайта и отправь мне.\n\n"
            "<i>Пример:</i>\n"
            "<code>Aqua, Glycerin, Niacinamide, Cetearyl Alcohol, "
            "Dimethicone, Tocopheryl Acetate, Parfum, Phenoxyethanol</code>",
            parse_mode=ParseMode.HTML
        )
    elif text == "🧴 Мой тип кожи":
        current = get_user_skin_type(user_id)
        status = f"Сейчас: <b>{SKIN_TYPES[current]['emoji']} {SKIN_TYPES[current]['name']}</b>" if current and current in SKIN_TYPES else "Сейчас: <i>не указан</i>"
        await update.message.reply_text(
            f"🧴 <b>Тип кожи</b>\n\n{status}\n\n"
            "Укажи свой тип — анализ будет персональным:",
            parse_mode=ParseMode.HTML,
            reply_markup=skin_type_keyboard()
        )
    elif text == "📊 История":
        await show_history(update, user_id)
    elif text == "ℹ️ О боте":
        users_count, analyses_count = get_stats()
        await update.message.reply_text(
            f"╔══════════════════════════╗\n"
            f"║   🔬 <b>SkinTruth</b> v{BOT_VERSION}        ║\n"
            f"╚══════════════════════════╝\n\n"
            f"AI-анализатор косметических составов.\n\n"
            f"🤖 <b>AI:</b> Llama 3.3 70B + Gemma 3 27B Vision\n"
            f"👥 <b>Пользователей:</b> {users_count}\n"
            f"🔬 <b>Анализов:</b> {analyses_count}\n\n"
            f"🔒 Бесплатно. Без рекламы. Без ограничений.\n\n"
            f"<i>Разработка: SkinTruth Team</i>\n"
            f"<i>Обратная связь: @Mario_Lalala</i>",
            parse_mode=ParseMode.HTML
        )
    else:
        return False  # Не наша кнопка
    return True


async def show_history(update_or_msg, user_id):
    """Показать историю анализов."""
    history = get_user_history(user_id)
    if not history:
        text = (
            "📊 <b>История анализов</b>\n\n"
            "<i>Пока нет анализов.</i>\n\n"
            "Отправь фото или текст состава для первого анализа!"
        )
    else:
        text = "📊 <b>История анализов</b>\n\n"
        for i, (inp_type, inp_text, score, created_at) in enumerate(history, 1):
            icon = "📸" if inp_type == "photo" else "✍️"
            score_display = f"<b>{score}/100</b>" if score else "—"
            short_text = inp_text[:40] + "..." if len(inp_text) > 40 else inp_text
            dt = created_at[:16].replace("T", " ") if created_at else "?"
            text += f"{i}. {icon} {score_display} • <i>{short_text}</i>\n   📅 {dt}\n\n"

    msg = update_or_msg.message if hasattr(update_or_msg, 'message') else update_or_msg
    await msg.reply_text(text, parse_mode=ParseMode.HTML)


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Анализ текстового состава."""
    text = update.message.text.strip()
    user = update.effective_user
    save_user(user)

    # Проверяем, не кнопка ли меню
    if text in ["📸 Анализ фото", "✍️ Анализ текста", "🧴 Мой тип кожи", "📊 История", "ℹ️ О боте"]:
        await handle_menu_buttons(update, context)
        return

    # Слишком короткий текст
    if len(text) < 8 and ',' not in text:
        await update.message.reply_text(
            "✍️ Отправь состав косметики текстом.\n\n"
            "<i>Пример:</i>\n"
            "<code>Aqua, Glycerin, Niacinamide, Dimethicone, Parfum</code>",
            parse_mode=ParseMode.HTML
        )
        return

    logger.info(f"Текст от {user.id} ({user.first_name}): {text[:60]}...")

    # Отправляем индикатор "печатает..."
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)

    msg = await update.message.reply_text(
        "⏳ <b>Анализирую состав...</b>\n\n"
        "🧪 AI изучает каждый ингредиент\n"
        "⏱️ ~10-30 секунд",
        parse_mode=ParseMode.HTML
    )

    # AI-анализ
    result = await ai_analyze_text(text, user.id)

    if result:
        # Извлекаем оценку из текста
        score = extract_score(result)
        save_analysis(user.id, "text", text, result, score)
        increment_analyses(user.id)

        # Удаляем сообщение "анализирую..."
        try:
            await msg.delete()
        except Exception:
            pass

        # Отправляем результат
        await send_long_message(update, result, after_analysis_keyboard())
    else:
        try:
            await msg.delete()
        except Exception:
            pass
        await update.message.reply_text(
            "⚠️ <b>AI временно недоступен</b>\n\n"
            "Попробуй через минуту или отправь другой состав.\n\n"
            "<i>Бесплатные AI-серверы иногда перегружены</i>",
            parse_mode=ParseMode.HTML
        )


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Анализ фото этикетки через AI Vision."""
    user = update.effective_user
    save_user(user)
    logger.info(f"Фото от {user.id} ({user.first_name})")

    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)

    msg = await update.message.reply_text(
        "📸 <b>Анализирую фото...</b>\n\n"
        "🔍 AI читает этикетку\n"
        "⏱️ ~15-40 секунд",
        parse_mode=ParseMode.HTML
    )

    try:
        # Скачиваем фото (самое большое разрешение)
        photo = update.message.photo[-1]
        file = await context.bot.get_file(photo.file_id)
        image_bytes = await file.download_as_bytearray()
        logger.info(f"Фото: {len(image_bytes)} байт, {photo.width}x{photo.height}")

        # AI Vision анализ
        result = await ai_analyze_photo(bytes(image_bytes), user.id)

        if result:
            score = extract_score(result)
            save_analysis(user.id, "photo", f"[фото {photo.width}x{photo.height}]", result, score)
            increment_analyses(user.id)

            try:
                await msg.delete()
            except Exception:
                pass

            await send_long_message(update, result, after_analysis_keyboard())
        else:
            try:
                await msg.delete()
            except Exception:
                pass
            await update.message.reply_text(
                "⚠️ <b>Не удалось обработать фото</b>\n\n"
                "Попробуй:\n"
                "• Сфотографировать ближе и чётче\n"
                "• Отправить при хорошем освещении\n"
                "• Или скопировать состав текстом\n\n"
                "<i>Бесплатные AI-серверы иногда перегружены</i>",
                parse_mode=ParseMode.HTML
            )

    except Exception as e:
        logger.error(f"Ошибка фото: {e}", exc_info=True)
        try:
            await msg.delete()
        except Exception:
            pass
        await update.message.reply_text(
            "⚠️ Ошибка при обработке фото. Попробуй ещё раз.",
            parse_mode=ParseMode.HTML
        )


async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка инлайн-кнопок."""
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data.startswith("skin_"):
        skin_key = data.replace("skin_", "")
        if skin_key == "skip":
            await query.message.reply_text(
                "👌 Пропущено. Можешь указать позже в меню.",
                parse_mode=ParseMode.HTML
            )
        elif skin_key in SKIN_TYPES:
            set_user_skin_type(user_id, skin_key)
            st = SKIN_TYPES[skin_key]
            await query.message.reply_text(
                f"✅ <b>Тип кожи сохранён!</b>\n\n"
                f"{st['emoji']} <b>{st['name']}</b> — {st['desc']}\n\n"
                f"Теперь все анализы будут учитывать ваш тип кожи "
                f"и давать персональные рекомендации.",
                parse_mode=ParseMode.HTML
            )

    elif data == "new_analysis":
        await query.message.reply_text(
            "🔬 <b>Новый анализ</b>\n\n"
            "Отправь:\n"
            "📸 <b>Фото</b> этикетки с составом\n"
            "✍️ <b>Текст</b> состава через запятую",
            parse_mode=ParseMode.HTML
        )

    elif data == "show_history":
        await show_history(query, user_id)

    elif data == "find_analog":
        await query.message.reply_text(
            "💡 <b>Подбор аналога</b>\n\n"
            "Отправь состав продукта, которому хочешь найти "
            "более безопасную или дешёвую замену.\n\n"
            "<i>Просто отправь состав как обычно — я подскажу альтернативы.</i>",
            parse_mode=ParseMode.HTML
        )

    elif data == "how_to":
        await query.message.reply_text(
            "❓ <b>Как пользоваться SkinTruth</b>\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "<b>Шаг 1.</b> Найди на упаковке раздел\n"
            "         <b>Ingredients</b> (Состав)\n\n"
            "<b>Шаг 2.</b> Сфотографируй или скопируй\n"
            "         текст с сайта магазина\n\n"
            "<b>Шаг 3.</b> Отправь мне — получи\n"
            "         <b>экспертный AI-разбор</b>!\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "💡 <b>Совет:</b> Укажи тип кожи 🧴\n"
            "для персональных рекомендаций",
            parse_mode=ParseMode.HTML
        )

    elif data == "choose_skin":
        current = get_user_skin_type(user_id)
        status = f"Сейчас: <b>{SKIN_TYPES[current]['emoji']} {SKIN_TYPES[current]['name']}</b>" if current and current in SKIN_TYPES else "Сейчас: <i>не указан</i>"
        await query.message.reply_text(
            f"🧴 <b>Тип кожи</b>\n\n{status}\n\nВыбери свой тип:",
            parse_mode=ParseMode.HTML,
            reply_markup=skin_type_keyboard()
        )


# ═══════════════ УТИЛИТЫ ═══════════════

def extract_score(text):
    """Извлечь оценку X/100 из текста AI."""
    match = re.search(r'(\d{1,3})\s*/\s*100', text)
    if match:
        return min(100, max(0, int(match.group(1))))
    return 0


def clean_html(text):
    """Убрать markdown-разметку, оставить только разрешённые HTML-теги."""
    # Убираем markdown bold **text** → <b>text</b>
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Убираем markdown italic *text* → <i>text</i>
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<i>\1</i>', text)
    # Убираем markdown headers
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    return text


async def send_long_message(update, text, keyboard=None):
    """Отправить длинное сообщение, разбив если нужно."""
    text = clean_html(text)

    # Telegram ограничение: 4096 символов
    if len(text) <= 4000:
        try:
            await update.message.reply_text(
                text, parse_mode=ParseMode.HTML, reply_markup=keyboard
            )
        except Exception as e:
            logger.warning(f"HTML ошибка, отправляю без формата: {e}")
            # Если HTML битый — убираем теги
            clean = re.sub(r'<[^>]+>', '', text)
            await update.message.reply_text(clean, reply_markup=keyboard)
    else:
        # Разбиваем на части
        parts = split_text(text, 4000)
        for i, part in enumerate(parts):
            kb = keyboard if i == len(parts) - 1 else None
            try:
                await update.message.reply_text(
                    part, parse_mode=ParseMode.HTML, reply_markup=kb
                )
            except Exception:
                clean = re.sub(r'<[^>]+>', '', part)
                await update.message.reply_text(clean, reply_markup=kb)


def split_text(text, max_len=4000):
    """Разбить текст на части по абзацам."""
    parts = []
    current = ""
    for line in text.split('\n'):
        if len(current) + len(line) + 1 > max_len:
            if current:
                parts.append(current)
            current = line
        else:
            current += ('\n' if current else '') + line
    if current:
        parts.append(current)
    return parts if parts else [text[:max_len]]


async def error_handler(update, context):
    """Глобальный обработчик ошибок."""
    logger.error(f"Ошибка: {context.error}", exc_info=context.error)
    try:
        if update and hasattr(update, 'effective_message') and update.effective_message:
            await update.effective_message.reply_text(
                "⚠️ Произошла ошибка. Попробуй ещё раз.",
                parse_mode=ParseMode.HTML
            )
    except Exception:
        pass


async def post_init(app):
    """Установить команды бота в меню Telegram."""
    commands = [
        BotCommand("start", "🏠 Главное меню"),
        BotCommand("help", "❓ Справка"),
    ]
    await app.bot.set_my_commands(commands)
    logger.info("Команды бота установлены")


# ═══════════════ HEALTH CHECK HTTP SERVER ═══════════════

class HealthHandler(BaseHTTPRequestHandler):
    """Простой HTTP-сервер для Render health check."""
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        users, analyses = get_stats()
        self.wfile.write(f"SkinTruth Bot v{BOT_VERSION} | Users: {users} | Analyses: {analyses}".encode())

    def log_message(self, format, *args):
        pass  # Без спама в логи


def start_health_server():
    """Запуск HTTP-сервера в фоне для Render."""
    server = HTTPServer(("0.0.0.0", PORT), HealthHandler)
    logger.info(f"🌐 Health-сервер на порту {PORT}")
    server.serve_forever()


# ═══════════════ ЗАПУСК ═══════════════

def main():
    logger.info("=" * 50)
    logger.info(f"🔬 SkinTruth v{BOT_VERSION} запускается...")
    logger.info(f"AI текст: {AI_MODEL_TEXT}")
    logger.info(f"AI фото:  {AI_MODEL_VISION}")
    logger.info(f"API ключ: {'✅ есть' if OPENROUTER_API_KEY else '❌ нет'}")
    logger.info("=" * 50)

    # Инициализация БД
    init_db()

    # Health check HTTP-сервер (для Render free tier)
    health_thread = threading.Thread(target=start_health_server, daemon=True)
    health_thread.start()

    # Сборка бота
    app = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .read_timeout(30)
        .write_timeout(30)
        .connect_timeout(15)
        .post_init(post_init)
        .build()
    )

    # Обработчики
    app.add_error_handler(error_handler)
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("help", cmd_help))
    app.add_handler(CallbackQueryHandler(handle_callback))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    logger.info("✅ Бот готов! Запуск polling...")
    app.run_polling(drop_pending_updates=False)


if __name__ == "__main__":
    main()
