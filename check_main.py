from settings import *
import subprocess
import os
import psutil

PATH = os.getcwd()

# Имя процесса, который нужно проверить
process_name = "mail_main.py"
scripts_path = PATH + "/" + process_name
python_executable = PATH + "/bin/python3"

# Получить список всех процессов Python
def is_process_running(process_name):
    bot.send_message(config['meid']['id'], "Bot verification")
    for proc in psutil.process_iter(["pid", "name"]):
        if process_name in proc.info["name"]:
            bot.send_message(config['meid']['id'], "The bot is working")
            return True
    bot.send_message(config['meid']['id'], "Bot doesn't work")
    return False

if not is_process_running(process_name):
    try:
        subprocess.check_call([python_executable, scripts_path])
    except:
        logging.error(traceback.format_exc())