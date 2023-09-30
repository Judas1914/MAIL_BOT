from settings import *
import subprocess
import os

# Имя процесса, который нужно проверить
process_name = "mail_main.py"

# Получить список всех процессов Python и поиск процесса с именем process_name
try:
    command = subprocess.check_output("ps aux | grep python", shell=True)
    all_proc = command.decode('utf-8').split("\n")
    finding_proc = False

    for proc in all_proc:
        if process_name in proc:
            finding_proc = True
            break

    if not finding_proc:
        # Процесс не найден, перезапустить его
        os.system("source ~/Bot/MAIL_BOT/bin/activate && cd ~/Bot/MAIL_BOT && nohup python mail_main.py &")
except Exception as e:
    logging.error(traceback.format_exc())
    print(f"Ошибка: {e}")
