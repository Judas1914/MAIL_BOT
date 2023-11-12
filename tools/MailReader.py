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
            for i in range(36):
                mail_txt.append(body[i])

        return(mail_txt)

def txt_form(mail_readed, i):
    if (i == 0):
        God_txt = (' '.join(mail_readed[:2]) + "\n\n"
                    + ' '.join(mail_readed[2:8]) + "\n"
                    + ' '.join(mail_readed[8:11]) + "\n\n"

                    + ' '.join(mail_readed[11:16]) + "\n"
                    + ' '.join(mail_readed[16:18]) + "\n\n"

                    + ' '.join(mail_readed[18:22]) + "\n"
                    + ' '.join(mail_readed[22:24]) + "\n\n"

                    + "Steam Guard: " + ''.join(mail_readed[26]))
    elif (i == 1):
        God_txt = (' '.join(mail_readed[:2]) + "\n\n"

                    + ' '.join(mail_readed[2:11]) + "\n"
                    + ' '.join(mail_readed[11:15]) + "\n\n"

                    + ' '.join(mail_readed[15:21]) + "\n"
                    + ' '.join(mail_readed[21:27]) + "\n\n"

                    + ' '.join(mail_readed[27:30]) + "\n"
                    + ' '.join(mail_readed[30:32]) + "\n\n")

        if (''.join(mail_readed[34]) == "Code"):
            God_txt += "Steam Guard: " + ''.join(mail_readed[35])
        elif (''.join(mail_readed[34]) == "If"):
            God_txt += "Steam Guard: " + ''.join(mail_readed[33])
        else:
            God_txt += "Steam Guard: " + ''.join(mail_readed[34])
        print(God_txt)

    return(God_txt)



