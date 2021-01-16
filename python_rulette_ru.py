import random


bets = ('Straight up (конкретное число )',
        'Column bet (колонка)',
        'Dozen bet (дюжина)',
        '1-18/19-36 (половина)',
        'Even/Odd (четные или нечетные)',
        'Red/Black (красное или черное)',
        'Любое число',
        # 'Split bet (три цифры)',
        # 'Corner bet (четыре числа)',
        # 'Street bet (ряд)',
        # 'Six line bet (два ряда)',
        )

score = 0

def roll(roll_number, bet_numbers, multiplier):
    print('Выпало: ', roll_number)
    if roll_number in bet_numbers:
        print('Поздравляем вы победили!!!\n'
              'Ваш выиграш: %s' % (bet_size * multiplier))
        return bet_size * multiplier
    else:
        print('Вы проиграли %s' % bet_size)
        return -bet_size

while True:
    print('Выберите тип ставки:')
    for b in range(len(bets)):
        print(b+1, ':', bets[b])

    bet_type = input('Bet type:')
    bet_size = int(input('Выберите размер ставки:'))
    bet_numbers = []
    roll_number = random.randint(0, 36)

    # 'Straight up (конкретное число )'
    if bet_type == '1':
        bet_numbers.append(int(input('Выберите ваше число от 0-36:')))
        if bet_numbers[0] not in range(37):
            raise NameError('Вы ввели неправильный символ')
        score += roll(roll_number, bet_numbers, 35)

    # 'Column bet (колонка)'
    elif bet_type == '2':
        first_column = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
        second_column = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
        third_column = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
        print(f'1: {first_column}\n'
              f'2: {second_column}\n'
              f'3: {third_column}')
        column = input('Выберите колонку:')
        if column == '1':
            bet_numbers = first_column
        elif column == '2':
            bet_numbers = second_column
        elif column == '3':
            bet_numbers = third_column
        else:
            print('Вы ввели неправильный тип ставки')
        score += roll(roll_number, bet_numbers, 2)

    # 'Dozen bet (дюжина)'
    elif bet_type == '3':
        print('1: 1-12\n'
              '2: 13-24\n'
              '3: 25-36')
        dozen = input('Выберите дюжину:')
        if dozen == '1':
            bet_numbers = range(1, 13)
        elif dozen == '2':
            bet_numbers = range(13, 25)
        elif dozen == '3':
            bet_numbers = range(25, 37)
        else:
            print('Вы ввели неправильный тип ставки')
        score += roll(roll_number, bet_numbers, 2)

    # '1-18/19-36 (половина)'
    elif bet_type == '4':
        print('1: 1-18\n'
              '2: 19-36')
        half = input('Выберите половину:')
        if half == '1':
            bet_numbers = range(1, 19)
        elif half == '2':
            bet_numbers = range(19, 37)
        else:
            print('Вы ввели неправильный тип ставки')
        score += roll(roll_number, bet_numbers, 1)

    # 'Even/Odd (четные или нечетные)'
    elif bet_type == '5':
        print('1: четные\n'
              '2: нечетные')
        half = input('Выберите половину:')
        if half == '1':
            bet_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
        elif half == '2':
            bet_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
        else:
            print('Вы ввели неправильный тип ставки')
        score += roll(roll_number, bet_numbers, 1)

    # 'Red/Black (красное или черное)'
    elif bet_type == '6':
        print('1: черные\n'
              '2: красные')
        half = input('Выберите цвет:')
        if half == '1':
            bet_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        elif half == '2':
            bet_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        else:
            print('Вы ввели неправильный тип ставки')
        score += roll(roll_number, bet_numbers, 1)

    # 'Любое число'
    elif bet_type == '7':
        amount = int(input('Введите количество чисел\n'
                            '1, 2, 3 или 4:'))
        if amount in (1, 2, 3, 4):
            for numb in range(amount):
                new_number = int(input('Введите число:'))
                while new_number in bet_numbers:
                    print(f'Вы повторили свое же число: {new_number}')
                    new_number = int(input('Введите другое число:'))
                bet_numbers.append(new_number)
            multiplier = 36/amount - 1
            score += roll(roll_number, bet_numbers, multiplier)
        else:
            print('Вы ввели неправильное количество чисел')
    else:
        print('Вы ввели неправильный тип ставки')
    print('Ваш счет: %s' % score)
