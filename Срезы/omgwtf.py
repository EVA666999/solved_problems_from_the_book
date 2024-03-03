import random

def main():
    file = open('pbnumbers.txt', 'w', encoding='utf-8')
    for _ in range(40):
            for _ in range(6):
                rn = str(random.randint(1, 69))
                file.write(rn + ' ')
            file.write('\n')
    file.close()


def tacke_common_numbers():
    file = open('pbnumbers.txt', 'r', encoding='utf-8')
    line = file.readline().rstrip('\n')
    result = []
    while line != '':
        result.append(line)
        line = file.readline().rstrip('\n')
    file.close()
    return result


def calc_common_numbers():
    result = tacke_common_numbers()
    a = ''
    for i in result:
        a += i
    lst = a.split()
    numbers_set = set(lst)
    numbers_count = dict.fromkeys(numbers_set, 0)

    for num in lst:
        numbers_count[num] += 1
    
    ress_max = []
    ress_min = []
    for key, value in numbers_count.items():
        if value >= 5:
            ress_max.append(key)
        elif value <= 2:
            ress_min.append(key)
    max_common_num = ress_max[6:]
    min_common_num = ress_min[7:]
    print(f'1.10 самых распространённых чисел!{sorted(max_common_num)}')
    print(f'2.10 самых нераспространённых чисел!{sorted(min_common_num)}')
    nums_26 = []
    for num in lst:
        if int(num) <= 26:
            nums_26.append(num)
    numbers_set1 = set(nums_26)
    numbers_count1 = dict.fromkeys(numbers_set1, 0)

    for num1 in numbers_set1:
        numbers_count1[num1] += 1
    print(f'3.Чистота чисел от 1-26{numbers_count1}')
    print(f'4.Чистота каждого числа от 1 до 69{numbers_count}')


print(calc_common_numbers())