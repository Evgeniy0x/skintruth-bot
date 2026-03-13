"""
SkinTruth — Калькулятор себестоимости ингредиентов.

Алгоритм:
- Ингредиенты в INCI идут по убыванию концентрации
- Вода (Aqua) обычно 60-80%
- Первые 5 ингредиентов = 70-80% формулы
- Рассчитываем для стандартной банки 50мл
"""
import logging

logger = logging.getLogger(__name__)

# Примерные концентрации по позиции в списке INCI
CONCENTRATION_MAP = {
    0: (55.0, 75.0),   # 1-й ингредиент (обычно вода)
    1: (5.0, 15.0),    # 2-й
    2: (3.0, 10.0),    # 3-й
    3: (2.0, 7.0),     # 4-й
    4: (1.0, 5.0),     # 5-й
    5: (0.5, 3.0),     # 6-й
    6: (0.5, 2.0),     # 7-й
    7: (0.3, 1.5),     # 8-й
    8: (0.2, 1.0),     # 9-й
    9: (0.1, 0.8),     # 10-й
}

# Для ингредиентов позиции 11+
DEFAULT_LATE_CONCENTRATION = (0.01, 0.5)

# Стандартный объём продукта (грамм)
STANDARD_WEIGHT_G = 50.0


def estimate_concentration(position: int) -> tuple[float, float]:
    """Оценка концентрации по позиции в списке INCI."""
    if position in CONCENTRATION_MAP:
        return CONCENTRATION_MAP[position]
    return DEFAULT_LATE_CONCENTRATION


def calculate_cost(ingredients_with_data: list, weight_g: float = STANDARD_WEIGHT_G) -> dict:
    """
    Рассчитать примерную себестоимость ингредиентов.

    Args:
        ingredients_with_data: список dict с полями:
            - name: название ингредиента
            - position: позиция в списке (0-based)
            - cost_per_gram: стоимость ₽/г (или None если не найден)
            - typical_concentration: типичная % концентрация (или None)

    Returns:
        dict с полями:
            - cost_min: минимальная оценка себестоимости (₽)
            - cost_max: максимальная оценка себестоимости (₽)
            - breakdown: список компонентов с оценками
            - retail_min: примерная мин. розничная цена
            - retail_max: примерная макс. розничная цена
    """
    total_min = 0.0
    total_max = 0.0
    breakdown = []

    for item in ingredients_with_data:
        position = item.get("position", 10)
        cost_per_gram = item.get("cost_per_gram")
        typical_conc = item.get("typical_concentration")

        if cost_per_gram is None or cost_per_gram <= 0:
            breakdown.append({
                "name": item["name"],
                "cost_min": 0,
                "cost_max": 0,
                "note": "стоимость неизвестна"
            })
            continue

        # Оцениваем концентрацию
        conc_min, conc_max = estimate_concentration(position)

        # Если есть типичная концентрация из базы — используем её как ориентир
        if typical_conc and typical_conc > 0:
            conc_min = min(conc_min, typical_conc * 0.5)
            conc_max = max(conc_max, typical_conc * 1.5)

        # Расчёт стоимости этого ингредиента
        grams_min = weight_g * (conc_min / 100)
        grams_max = weight_g * (conc_max / 100)

        ingredient_cost_min = grams_min * cost_per_gram
        ingredient_cost_max = grams_max * cost_per_gram

        total_min += ingredient_cost_min
        total_max += ingredient_cost_max

        breakdown.append({
            "name": item["name"],
            "cost_min": round(ingredient_cost_min, 2),
            "cost_max": round(ingredient_cost_max, 2),
            "concentration_range": f"{conc_min:.1f}-{conc_max:.1f}%"
        })

    # Добавляем стоимость упаковки (~20-50₽)
    packaging_min = 20
    packaging_max = 50
    total_min += packaging_min
    total_max += packaging_max

    # Розничная цена (наценка 5-15x)
    retail_min = round(total_min * 5)
    retail_max = round(total_max * 15)

    return {
        "cost_min": round(total_min),
        "cost_max": round(total_max),
        "breakdown": breakdown,
        "retail_min": retail_min,
        "retail_max": retail_max,
        "packaging": f"{packaging_min}-{packaging_max}"
    }


def format_markup_comment(cost_min: int, cost_max: int) -> str:
    """Комментарий о наценке."""
    avg_cost = (cost_min + cost_max) / 2

    if avg_cost < 50:
        return "💡 Себестоимость очень низкая — типичная наценка может достигать 3000-5000%!"
    elif avg_cost < 150:
        return "💡 Средняя себестоимость. Наценка в рознице обычно 500-1500%."
    elif avg_cost < 500:
        return "💡 Выше средней себестоимости — скорее всего, продукт содержит качественные активы."
    else:
        return "💡 Высокая себестоимость — в составе дорогие активные ингредиенты."
