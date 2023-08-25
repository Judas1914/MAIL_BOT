from settings import *

token = config['Telegram']['token']
bot = telebot.TeleBot(token)
chat_id = '-1001919822446'

mail = config_mail['Email']['mail']
password = config_mail['Email']['pass']

mail_ref = "вы пытаетесь войти в аккаунт с нового устройства"

def mail_reader():
    email_id_list = email_ids[0].split()

    if len(email_id_list) > 0:
        status, email_data = imap.fetch(email_id_list[0], "RFC822")


        if str(email_data[0][1]).isdigit() == "1":
            msg = email_data[1][1].decode('utf-8')

        else:
            status, email_data = imap.fetch(email_id_list[0], "RFC822")
            msg = email_data[0][1].decode('utf-8')

        message = email.message_from_string(msg)

        if message.is_multipart():
            for part in message.get_payload():
                body = part.get_payload(decode=True).decode('UTF-8').split()
                break

        mail_txt = []
        mail_inf = []

        for i in range(27):
            mail_txt.append(body[i])

        return(mail_txt)


while True:
    imap = imaplib.IMAP4_SSL("imap.mail.ru")

    imap.login(mail, password)
    imap.select("Steam")

    status, email_ids = imap.search(None, 'UNSEEN')
    email_id_list = email_ids[0].split()

    imap.logout

    if len(email_id_list) > 0:
        mail_readed = mail_reader()
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

