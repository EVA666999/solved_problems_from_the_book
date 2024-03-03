import random

my_dict = {
    'два пик': 2,
    'три пик': 3,
    'четыре пик': 4,
    'пять пик': 5,
    'шесть пик': 6,
    'семь пик': 7,
    'восемь пик': 8,
    'девять пик': 9,
    'десять пик': 10,
    'валет пик': 10,
    'дама пик': 10,
    'король пик': 10,
    'туз пик': (1, 11),  # Туз может быть 1 или 11
    'два червей': 2,
    'три червей': 3,
    'четыре червей': 4,
    'пять червей': 5,
    'шесть червей': 6,
    'семь червей': 7,
    'восемь червей': 8,
    'девять червей': 9,
    'десять червей': 10,
    'валет червей': 10,
    'дама червей': 10,
    'король червей': 10,
    'туз червей': (1, 11),
    'два бубей': 2,
    'три бубей': 3,
    'четыре бубей': 4,
    'пять бубей': 5,
    'шесть бубей': 6,
    'семь бубей': 7,
    'восемь бубей': 8,
    'девять бубей': 9,
    'десять бубей': 10,
    'валет бубей': 10,
    'дама бубей': 10,
    'король бубей': 10,
    'туз бубей': (1, 11),
    'два треф': 2,
    'три треф': 3,
    'четыре треф': 4,
    'пять треф': 5,
    'шесть треф': 6,
    'семь треф': 7,
    'восемь треф': 8,
    'девять треф': 9,
    'десять треф': 10,
    'валет треф': 10,
    'дама треф': 10,
    'король треф': 10,
    'туз треф': (1, 11),
}

def player1():
    p1 = []
    res_for_sum = []
    random_key, random_value = random.choice(list(my_dict.items()))
    if random_key == 'туз треф' or random_key == 'туз бубей' or random_key == 'туз червей' or random_key == 'туз пик':
        num = int(input('Выберите значение 1-11: '))
        random_value = num
        p1.append((random_key, random_value))
    ask = 'да'
    while ask.lower() != 'нет':
        random_key, random_value = random.choice(list(my_dict.items()))
        if random_key == 'туз треф' or random_key == 'туз бубей' or random_key == 'туз червей' or random_key == 'туз пик':
            num = int(input('Выберите значение 1-11: '))
            random_value = num
            p1.append((random_key, random_value))
        else:
            p1.append((random_key, random_value))
        print(f'Ваша колода карт: {p1}')
        ask = input('Хочешь добавить карту? да-нет: ')
        print(f'Ваша колода карт: {p1}')
    for i in p1:
        res_for_sum.append(i[-1])
    return sum(res_for_sum)


def player2():
    p1 = []
    res_for_sum = []
    random_key, random_value = random.choice(list(my_dict.items()))
    if random_key == 'туз треф' or random_key == 'туз бубей' or random_key == 'туз червей' or random_key == 'туз пик':
        num = int(input('Выберите значение 1-11: '))
        random_value = num
        p1.append((random_key, random_value))
    ask = 'да'
    while ask.lower() != 'нет':
        random_key, random_value = random.choice(list(my_dict.items()))
        if random_key == 'туз треф' or random_key == 'туз бубей' or random_key == 'туз червей' or random_key == 'туз пик':
            num = int(input('Выберите значение 1-11: '))
            random_value = num
            p1.append((random_key, random_value))
        else:
            p1.append((random_key, random_value))
        print(f'Ваша колода карт: {p1}')
        ask = input('Хочешь добавить карту? да-нет: ')
        print(f'Ваша колода карт: {p1}')
    for i in p1:
        res_for_sum.append(i[-1])
    return sum(res_for_sum)


def game():
    p1 = player1()
    p2 = player2()
    if p1 == 21:
        return f'{p1} Win player1'
    elif p2 == 21:
        return f'{p2} Win player2'
    elif p1 > p2 and p1 < 21:
        return f'{p1} Win player1 and sum player2 = {p2}'
    elif p2 > p1 and p2 < 21:
        return f'{p2} Win player2 and sum player1 = {p1}'
    elif p1 > 21 and p2 < p1:
        return f'{p2} Win player2 and sum player1 = {p1}'
    elif p2 > 21 and p1 < p2:
        return f'{p1} Win player1 and sum player2 = {p2}'
print(game())