import random

def countrys():
    my_dict = {}
    citys = ['Айдахо', 'Айова', 'Алабама']
    countrys = ['Центр Бойсе', 'Основной центр Де-Мойн', 'Монтгомери']
    my_dict = {k:v for (k, v) in zip(citys, countrys)}
    country = random.choice(citys)
    ask = input(f'Введите столицу для:{country}')
    correct = 0
    uncorrect = 0
    while ask.lower() != 'н':
        if my_dict[country] == ask:
            correct += 1
            print(f'Win:{correct}')
        else:
            uncorrect += 1
            print(f'Вы проиграли ъыъы: {uncorrect}')
        country = random.choice(citys)
        ask = input(f'Введите столицу для:{country}')

print(countrys())