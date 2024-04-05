from settings import *

mail_clone = ['Dear', 'Pepe,', 'It', 'looks', 'like',
              'you', 'are', 'trying', 'to', 'log', 'in', 'from',
              'a', 'new', 'device.', 'Here', 'is', 'the', 'Steam',
              'Guard', 'code', 'you', 'need', 'to', 'access', 'your',
              'account:', 'Request', 'made', 'from', 'Space', 'station',
              'Login', 'Code', '@@@@@', 'If']

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
            for i in range(40):
                mail_txt.append(body[i])

        return(mail_txt)

def txt_form(mail_readed, i):
    God_txt = 0
    if (i == 0):
        God_txt = (' '.join(mail_readed[:2]) + "\n\n"

                    + ' '.join(mail_readed[2:8]) + "\n"
                    + ' '.join(mail_readed[8:11]) + "\n\n"

                    + ' '.join(mail_readed[11:16]) + "\n"
                    + ' '.join(mail_readed[16:18]) + "\n\n"

                    + ' '.join(mail_readed[18:22]) + "\n"
                    + ' '.join(mail_readed[mail_readed.index("страны:"):mail_readed.index("Код")]) + "\n\n"

                    + "Steam Guard: " + ''.join(mail_readed[mail_readed.index("доступа") + 1]))

    elif (i == 1):
        God_txt = (' '.join(mail_readed[:2]) + "\n\n"

                    + ' '.join(mail_readed[2:11]) + "\n"
                    + ' '.join(mail_readed[11:15]) + "\n\n"

                    + ' '.join(mail_readed[15:21]) + "\n"
                    + ' '.join(mail_readed[21:27]) + "\n\n"

                    + ' '.join(mail_readed[27:30]) + "\n"
                    + ' '.join(mail_readed[mail_readed.index("made") + 2:mail_readed.index("Login")]) + "\n\n"

                    + "Steam Guard: " + ''.join(mail_readed[mail_readed.index("Code") + 1]))

    elif (i == 2): # - Тайский
        God_txt = (''.join(mail_clone[0]) + " " + ''.join(mail_readed[1]) + "\n\n"

                    + ' '.join(mail_clone[2:11]) + "\n"
                    + ' '.join(mail_clone[11:15]) + "\n\n"

                    + ' '.join(mail_clone[15:21]) + "\n"
                    + ' '.join(mail_clone[21:27]) + "\n\n"

                    + ' '.join(mail_clone[27:30]) + "\n"
                    + ''.join("Thailand") + "\n\n"

                    + "Steam Guard: " + ''.join(mail_readed[mail_readed.index("รหัสการเข้าสู่ระบบ") + 1]))

    elif (i == 3): # - Португальский
        God_txt = (''.join(mail_clone[0]) + " " + ''.join(mail_readed[1]) + "\n\n"

                    + ' '.join(mail_clone[2:11]) + "\n"
                    + ' '.join(mail_clone[11:15]) + "\n\n"

                    + ' '.join(mail_clone[15:21]) + "\n"
                    + ' '.join(mail_clone[21:27]) + "\n\n"

                    + ' '.join(mail_clone[27:30]) + "\n"
                    + ' '.join(mail_readed[mail_readed.index("solicitação:"):mail_readed.index("autenticação") - 2]) + "\n\n"

                    + "Steam Guard: " + ''.join(mail_readed[mail_readed.index("autenticação") + 1]))

    elif (i == 4): # - Украинский
        God_txt = (''.join(mail_readed[0]) + " " + ''.join(mail_readed[1]) + "\n\n"

                    + ' '.join(mail_readed[2:6]) + "\n"
                    + ' '.join(mail_readed[6:9]) + "\n\n"

                    + ' '.join(mail_readed[9:12]) + "\n"
                    + ' '.join(mail_readed[15:20]) + "\n\n"

                    + ' '.join(mail_readed[21:25]) + "\n"
                    + ' '.join(mail_readed[mail_readed.index("цієї") + 2:mail_readed.index("Код")]) + "\n\n"

                   + "Steam Guard: " + ''.join(mail_readed[mail_readed.index("входу") + 1]))

    return(God_txt)



