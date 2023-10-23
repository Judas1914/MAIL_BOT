from settings import *

def mail_reader(imap: imaplib.IMAP4_SSL, email_ids: list):
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
                try:

                    Flag = True
                    body = part.get_payload(decode=True).decode('UTF-8').split()
                    break

                except:

                    Flag = False
                    break

        mail_txt = []
        mail_inf = []

        if Flag:
            for i in range(27):
                mail_txt.append(body[i])

        return(mail_txt)

def txt_form(mail_readed):
    God_txt = (' '.join(mail_readed[:2]) + "\n\n"
                + ' '.join(mail_readed[2:8]) + "\n"
                + ' '.join(mail_readed[8:11]) + "\n\n"

                + ' '.join(mail_readed[11:16]) + "\n"
                + ' '.join(mail_readed[16:18]) + "\n\n"

                + ' '.join(mail_readed[18:22]) + "\n"
                + ' '.join(mail_readed[22:24]) + "\n\n"

                + "Steam Guard: " + ''.join(mail_readed[26]))
    return(God_txt)



