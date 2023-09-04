import subprocess
import os

command = subprocess.check_output("ps aux | grep python", shell=True)
all_proc = command.decode('utf-8').split("\n") 
finding_proc = False

for proc in all_proc:
    if "mail_main" in proc:
        finding_proc = True

if finding_proc == False:
    os.system("nohup source Bot/MAIL_BOT/bin/activate && python mail_main.py")