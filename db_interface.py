import telebot
from threading import Thread
from config import token, bot_base
from mongoengine import connect
from models import User, Bet, Text
from telebot.types import (InlineKeyboardButton,
                           InlineKeyboardMarkup,
                           ReplyKeyboardMarkup)
import time

connect(bot_base)

Text(title='rules', date=time.strftime("%y.%m.%d (%H:%M:%S)"), type='rules',
     text='Просле нажатия кнопки "Рулетка" начинаеся игра').save()