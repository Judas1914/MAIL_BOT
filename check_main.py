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
    for proc in psutil.process_iter(["pid", "name"]):
        if process_name in proc.info["name"]:
            return True
    return False

if not is_process_running(process_name):
    try:
        subprocess.check_call([python_executable, scripts_path])
    except:
        logging.error(traceback.format_exc())