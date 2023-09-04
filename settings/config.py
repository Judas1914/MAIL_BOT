# Для бота
from aiogram.dispatcher import Dispatcher
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import telebot
import traceback
import imaplib
import email
from email.header import decode_header
import base64
from bs4 import BeautifulSoup
import re

# Стандарт
import re
import configparser
import time

settings_file = "settings"
config = configparser.ConfigParser()
config.read('settings/settings.ini')

mail_file = "mail"
config_mail = configparser.ConfigParser()
config_mail.read('settings/mail.ini')

def config_update():
    with open(settings_file, 'w') as fl:
        config.write(fl)
    config.read(settings_file)

def config_update():
    with open(mail_file, 'w') as fl:
        config_mail.write(fl)
    config_mail.read(mail_file)


# Бот
token = config['Telegram']['token']
bot = telebot.TeleBot(token)

# Почта
imap = imaplib.IMAP4_SSL("imap.mail.ru")

# Логгер
import logging
logging.basicConfig(
    level=logging.INFO,
    filename="logs.log",
    format="%(asctime)s - %(module)s\n[%(levelname)s] %(funcName)s:\n %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    encoding="utf-8"

)

"""
Места где может произойти ошибка помечай как 
try:
    <блок кода>
except:
    logging.error(traceback.format_exc())
"""