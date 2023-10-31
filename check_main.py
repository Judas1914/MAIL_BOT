from settings import *
import psutil
import subprocess
import os
import time

PATH = os.getcwd()

process_name = "mail_main.py"
scripts_path = PATH + "/" + process_name
python_executable = PATH + "/bin/python3"

while True:
    time.sleep(300)
    for proc in psutil.process_iter(["pid", "name"]): # Получить список всех процессов Python
        if process_name in proc.info["name"]:
            bot.send_message(config['meid']['id'], "The bot is working")
            break
        else:
            bot.send_message(config['meid']['id'], "Bot reset")
            try:
                subprocess.check_call([python_executable, scripts_path])
            except:
                logging.error(traceback.format_exc())