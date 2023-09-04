from settings import *
from tools import *


if __name__ == '__main__':
    try:
        chat_id = config['chat']['id']
        mail = config_mail['Email']['mail']
        password = config_mail['Email']['pass']
        mail_ref = "вы пытаетесь войти в аккаунт с нового устройства"
        imap.login(mail, password)

        while True:
            imap.select("Steam")
            status, email_ids = imap.search(None, 'UNSEEN')
            email_id_list = email_ids[0].split()


            if len(email_id_list) > 0:
                mail_readed = mail_reader(imap, email_ids)
                if mail_ref in " ".join(mail_readed):
                    God_txt = (' '.join(mail_readed[:2]) + "\n\n"

                            + ' '.join(mail_readed[2:8]) + "\n"
                            + ' '.join(mail_readed[8:11]) + "\n\n"

                            + ' '.join(mail_readed[11:16]) + "\n"
                            + ' '.join(mail_readed[16:18]) + "\n\n"

                            + ' '.join(mail_readed[18:22]) + "\n"
                            + ' '.join(mail_readed[22:24]) + "\n\n"

                            + "Steam Guard: " + ''.join(mail_readed[26]))
                    bot.send_message(chat_id, God_txt)
                time.sleep(10)
            time.sleep(10)
    except:
        logging.error(traceback.format_exc())




