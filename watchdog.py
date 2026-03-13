"""
Watchdog — перезапускает бота если он упал.
Работает как отдельный процесс.
"""
import subprocess
import time
import sys
import os

BOT_SCRIPT = os.path.join(os.path.dirname(__file__), "bot_final.py")
LOG_FILE = os.path.join(os.path.dirname(__file__), "watchdog.log")

def log(msg):
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")

def main():
    log("🐕 Watchdog запущен")
    restart_count = 0

    while True:
        restart_count += 1
        log(f"🔄 Запуск бота (попытка #{restart_count})...")

        try:
            proc = subprocess.Popen(
                [sys.executable, BOT_SCRIPT],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                cwd=os.path.dirname(__file__)
            )
            log(f"✅ Бот запущен, PID: {proc.pid}")

            # Ждём завершения
            proc.wait()
            exit_code = proc.returncode
            log(f"⚠️ Бот завершился с кодом {exit_code}")

        except Exception as e:
            log(f"❌ Ошибка запуска: {e}")

        # Пауза перед перезапуском (25 сек — cooldown Telegram)
        wait_time = 25
        log(f"⏳ Жду {wait_time} сек перед перезапуском...")
        time.sleep(wait_time)

if __name__ == "__main__":
    main()
