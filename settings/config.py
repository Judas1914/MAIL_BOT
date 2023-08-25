# Для бота
from aiogram.dispatcher import Dispatcher
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import telebot

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


