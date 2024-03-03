import random

def main():
    file = open('score.txt', 'w', encoding='utf-8')
    yes_or_no = 'да'
    while yes_or_no != 'н':
        ask = input('Введите оценки ученака')
        file.write(f'{ask}\n')
        yes_or_no = input('Введите да если хотите добавить ученика')
    file.close()


def avarege_score():
    file = open('score.txt', 'r', encoding='utf-8')
    line = file.readline()
    total = 0
    line = line.rstrip('\n')
    for i in line:
        tokens = i.split(',')
    for j in tokens:
        total += int(j)
    avg = total / len(tokens)
    print(avg)
    file.close()


print(avarege_score())