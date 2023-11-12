from settings import *
from tools import *


if __name__ == '__main__':
    bot.send_message(config['meid']['id'], "Bot on")
    try:
        chat_id = config['chat']['id']
        mail = config_mail['Email']['mail']
        password = config_mail['Email']['pass']
        mail_ref = ["вы пытаетесь войти в аккаунт с нового устройства","It looks like you are trying to log in from a new device"]
        imap.login(mail, password)

        while True:
            imap.select("Steam")
            status, email_ids = imap.search(None, 'UNSEEN')
            email_id_list = email_ids[0].split()


            if len(email_id_list) > 0:
                mail_readed = mail_reader(imap, email_ids)
                for i in range(len(mail_ref)):
                    if mail_ref[i] in " ".join(mail_readed):
                        txt = txt_form(mail_readed, i)
                        bot.send_message(chat_id, txt)
    except:
        bot.send_message(config['meid']['id'], "Bot off")
        logging.error(traceback.format_exc())




