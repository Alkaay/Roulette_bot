import random
import telebot
from config import token, bot_base
from mongoengine import connect
from models import User, Bet
import time


bot = telebot.TeleBot(token)
connect(bot_base)


def roll(seconds):
    while True:
        print('new roll')
        roll_number = random.randint(0, 36)
        bets = Bet.objects.filter(result=0)
        red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        if roll_number in red_numbers:
            color = 'Красное'
        elif roll_number in black_numbers:
            color = 'Черное'
        elif roll_number == 0:
            color = 'Зеленое'
        for bet in bets:
            user = bet.user
            if roll_number in bet.bet_numbers:
                win_size = round(bet.bet_size * (36 / len(bet.bet_numbers) - 1))
                user.count += win_size
                bet.result = 1
                bet.save()
                user.save()
                bot.send_message(user.user_id, text=f'Шарик остановился на {roll_number} {color}\n'
                                                    f'😃Поздравляем вы победили!!!😃\n'
                                                    f'Выиграш: {win_size}$\n'
                                                    f'Счет: {bet.user.count}$',)

            else:
                user.count -= bet.bet_size
                bet.result = -1
                bet.save()
                user.save()
                bot.send_message(bet.user.user_id, text=f'Шарик остановился на {roll_number} {color}\n'
                                                        f'😞Вы проиграли😞\n'
                                                        f'Проигрыш: {bet.bet_size}$\n'
                                                        f'Счет: {bet.user.count}$',)
        time.sleep(seconds)

