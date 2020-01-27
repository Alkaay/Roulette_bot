import telebot
from config import token, bot_base
from mongoengine import connect
from models import User, Bet, Text
from telebot.types import (InlineKeyboardButton,
                           InlineKeyboardMarkup,
                           ReplyKeyboardMarkup)
import time

bot = telebot.TeleBot(token)
connect(bot_base)

#Roll Thread-----------------------------------------------------------------
from threading import Thread
from rolling import roll
roll_thread = Thread(target=roll, args=(10,))
roll_thread.start()
print('Rolling started')

#Keyboards-----------------------------------------------------------------
start_keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
start_keyboard.add('Рулетка',
                   # 'Инфо',
                   )

#Functions-----------------------------------------------------------------
def bet_type_chose(message_or_call, next_call_data):
    bets = ('Число',
            'Красн/черн',
            # 'Колонка',
            # 'Дюжина',
            # 'Половина',
            # 'Чет/нечет',
            # 'До 4х чисел',
            )
    bets_kb = InlineKeyboardMarkup(row_width=3)
    buttons_list = []

    for bet in bets:
        buttons_list.append(InlineKeyboardButton(
            text=bet, callback_data=f'{next_call_data}_' + str(bets.index(bet)+1)))
    bets_kb.add(*buttons_list)
    bot.send_message(message_or_call.chat.id, text='Выберите тип ставки:',
                     reply_markup=bets_kb)


def bet_choyse(call, next_call_data, bet_size=''):
    if bet_size != '':
        bet_size += '_'

    if call.data.split('_')[1] == '1':
        bet_numbers_kb = InlineKeyboardMarkup(row_width=3)
        buttons_list = []
        numbers = {'36': '🔴', '35': '⚫', '34': '🔴', '33': '⚫', '32': '🔴', '31': '⚫', '30': '🔴', '29': '⚫',
                   '28': '⚫', '27': '🔴', '26': '⚫', '25': '🔴', '24': '⚫', '23': '🔴', '22': '⚫', '21': '🔴',
                   '20': '⚫', '19': '🔴', '18': '🔴', '17': '⚫', '16': '🔴', '15': '⚫', '14': '🔴', '13': '⚫',
                   '12': '🔴', '11': '⚫', '10': '⚫', '9': '🔴', '8': '⚫', '7': '🔴', '6': '⚫', '5': '🔴', '4': '⚫',
                   '3': '🔴', '2': '⚫', '1': '🔴', '0': '🍏'}
        for bet_number, bet_color in numbers.items():
            buttons_list.append(InlineKeyboardButton(
                text=bet_number+bet_color,
                callback_data=f'{next_call_data}_' + bet_size + str(bet_number)))
        bet_numbers_kb.add(*buttons_list)
        bot.send_message(call.message.chat.id, text='Выберите ваше число:',
                         reply_markup=bet_numbers_kb)
    elif call.data.split('_')[1] == '2':
        bet_color_kb = InlineKeyboardMarkup(row_width=3)
        buttons_list = []
        colors = ('Красное', 'Черное')
        for bet_color in colors:
            buttons_list.append(InlineKeyboardButton(
                text=bet_color, callback_data=f'{next_call_data}_' + bet_size + bet_color))
        bet_color_kb.add(*buttons_list)
        bot.send_message(call.message.chat.id, text='Выберите цвет ставки:',
                         reply_markup=bet_color_kb)


def bet_size(bet_type=None, call=None, message=None):
    if call:
        bet_type = call.data.split('_')[1]
        call_or_message = call.message
    else:
        call_or_message = message
    bet_size_kb = InlineKeyboardMarkup(row_width=4)
    buttons_list = []
    sizes = (1, 5, 10, 15)
    for bet_size in sizes:
        buttons_list.append(InlineKeyboardButton(
            text=f'{bet_size}$', callback_data='bet_' + str(bet_size) + '_' + bet_type))
    bet_size_kb.add(*buttons_list)
    bot.send_message(call_or_message.chat.id, text='Выберите размер ставки:',
                     reply_markup=bet_size_kb)

#Handlers-----------------------------------------------------------------
@bot.message_handler(commands=['start'])
def start(message):
    user = User.get_or_create_user(message)
    if message.from_user.first_name:
        name = ' ' + message.from_user.first_name
    else:
        name = ''
    bot.send_message(message.chat.id, text=f'Здраствуйте{name}. Увас на счету {user.count}$. Готовы сыграть?',
                     reply_markup=start_keyboard)

@bot.message_handler(regexp='Инфо')
def count(message):
    info_kb = InlineKeyboardMarkup(row_width=2)
    buttons_list = []
    buttons_list.append(InlineKeyboardButton(text='Новости', callback_data='News'))
    # buttons_list.append(InlineKeyboardButton(text='Правила', callback_data='Rules'))
    info_kb.add(*buttons_list)
    bot.send_message(message.chat.id, text='Выберите тип ставки:',
                     reply_markup=info_kb)

@bot.message_handler(regexp='В главное меню')
def count(message):
    user = User.get_or_create_user(message)
    bot.send_message(message.chat.id, text=f'Увас на счету {user.count}$.',
                     reply_markup=start_keyboard)

@bot.message_handler(func=lambda message: message.text == 'Рулетка' or message.text =='Новая ставка')
def bet_type_chose_handler(message):
    next_call_data = 'bet type'
    bet_type_chose(message, next_call_data)

@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'bet type')
def bet_choyse_handler(call):
    next_call_data = 'bet choice'
    bet_choyse(call, next_call_data)

@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'bet choice')
def bet_size_handler(call):
    bet_size(call=call)


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'bet')
def bet_saver(call):
    roulette_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    roulette_kb.add('Повторить', 'На что то другое', 'Новая ставка', 'Изменить сумму ставки', 'В главное меню')

    user = User.get_user(call.from_user.id)
    bet_size = call.data.split('_')[1]
    call_bet_type = call.data.split("_")[2]

    if call_bet_type == 'Черное':
        bet_type = call_bet_type
        bet_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        in_message_bet = bet_type
    elif call_bet_type == 'Красное':
        bet_type = call_bet_type
        bet_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        in_message_bet = bet_type
    else:
        str_bet_numbers = call_bet_type.split(',')
        bet_numbers = []
        for n in str_bet_numbers:
            bet_numbers.append(int(n))
        bet_type = 'Число(а)'
        in_message_bet = call_bet_type

    Bet(user=user, bet_size=bet_size, bet_numbers=bet_numbers, bet_type=bet_type,
        date=time.strftime("%y.%m.%d (%H:%M:%S)")).save()
    print('New bet from:' + str(user.nickname))
    bot.send_message(call.message.chat.id, text=f'Ставка принята:\n'
                                                f'{bet_size}$ на "{in_message_bet}"',
                     reply_markup=roulette_kb)


@bot.message_handler(regexp='Повторить')
def lust_bet_repeet(message):
    user = User.get_user(message.from_user.id)
    last_bet = Bet.objects.filter(user=user).order_by('-date').first()
    bet_size = last_bet.bet_size
    bet_numbers = last_bet.bet_numbers
    bet_type = last_bet.bet_type

    Bet(user=user, bet_size=bet_size, bet_numbers=bet_numbers, bet_type=bet_type,
        date=time.strftime("%y.%m.%d (%H:%M:%S)")).save()
    print('New bet from:' + str(user.nickname))

    if bet_type == 'Число(а)':
        bet_type = ''
        for number in bet_numbers:
            bet_type += f'{number}'
    bot.send_message(message.chat.id, text=f'Ставка принята:\n'
                                           f'{bet_size}$ на "{bet_type}"')

@bot.message_handler(regexp='На что то другое')
def bet_type_change_1st_step(message):
    next_call_data = 'bet type change'
    bet_type_chose(message, next_call_data)

@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'bet type change')
def bet_type_change_2st_step(call):
    user = User.get_user(call.from_user.id)
    last_bet = Bet.objects.filter(user=user).order_by('-date').first()
    bet_size = str(last_bet.bet_size)
    next_call_data = 'bet'
    bet_choyse(call, next_call_data, bet_size)

@bot.message_handler(regexp='Изменить сумму ставки')
def bet_size_change_handler(message):
    user = User.get_user(message.from_user.id)
    last_bet = Bet.objects.filter(user=user).order_by('-date').first()
    if last_bet.bet_type == 'Число(а)':
        bet_type = ''
        for bet in last_bet.bet_numbers:
           bet_type += bet
    else:
        bet_type = last_bet.bet_type
    bet_size(bet_type=bet_type, message=message)

#--------------------------------------------------------------------------------------------------------------

print("Bot started")
bot.polling(none_stop=True)
