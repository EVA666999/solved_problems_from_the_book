import random

def main():
    days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    mouths = ['07', '14', '21', '27']
    years = ['1993', '1994', '1995']
    file = open('gasprices.txt', 'w', encoding='utf-8')

    for y in years:
        for d in days:
            for m in mouths:
                rn = random.uniform(1, 1.9)
                formatted_number = "{:.3f}".format(rn)
                file.write(f'{d}-{m}-{y}:{formatted_number}\n')

    file.close()


def calc_avg_price_for_year():
    days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    file = open('gasprices.txt', 'r', encoding='utf-8')
    price = file.readline().rstrip('\n')
    result = []
    total = 0
    first_year_1993 = []
    second_year_1994 = []
    third_year_1995 = []
    sum_for_m_1993 = []
    sum_for_m_1994 = []
    sum_for_m_1995 = []
    sorted_all_prices = []

    while price != '':
        result.append(price)
        sorted_all_prices.append(price[-5:])

        for i in days:
            if i in price[:2] and '1993' in price:
                first_year_1993.append(float(price[-5:]))
                sum_for_m_1993.append(price[11:])
            elif i in price[:2] and '1994' in price:
                second_year_1994.append(float(price[-5:]))
                sum_for_m_1994.append(price[11:])
            elif i in price[:2] and '1995' in price:
                third_year_1995.append(float(price[-5:]))
                sum_for_m_1995.append(price[11:])
        avg_1993 = sum(first_year_1993) / len(first_year_1993) if len(first_year_1993) > 0 else 0
        avg_1994 = sum(second_year_1994) / len(second_year_1994) if len(second_year_1994) > 0 else 0
        avg_1995 = sum(third_year_1995) / len(third_year_1995) if len(third_year_1995) > 0 else 0
        price = file.readline().rstrip('\n')
    
    i = 0
    a = 0
    while i < len(sum_for_m_1993):
        file_sum = [float(x) for x in sum_for_m_1993[i:i+4]] # срез первые 4 елемента в итерацие тоестть есои список a = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] вывод будет a b c d 
        d = sum(file_sum) # а тут мы сумируем 4 елемента 
        a += 1
        print(f'Сумма месяца{a} - 1993 года: {d}')
        i += 4 # шаг в 4 елемента

    i = 0
    a = 0
    while i < len(sum_for_m_1994):
        file_sum = [float(x) for x in sum_for_m_1994[i:i+4]]
        d = sum(file_sum)
        a += 1
        print(f'Сумма месяца{a} - 1994года: {d}')
        i += 4

    i = 0
    a = 0
    while i < len(sum_for_m_1995):
        file_sum = [float(x) for x in sum_for_m_1995[i:i+4]]
        d = sum(file_sum)
        a += 1
        print(f'Сумма месяца{a} - 1995года: {d}')
        i += 4

    file.close()
    return avg_1993, avg_1994, avg_1995, f'Наименьшая цена в 1993 году составила:{min(first_year_1993)}', f'Наименьшая цена в 1994 году составила:{min(second_year_1994)}', f'Наименьшая цена в 1995 году составила:{min(third_year_1995)}, отсортированые цены: {sorted(sorted_all_prices)}, список цен упорядоченых по увеличению: {sorted_all_prices[::-1]}'
print(calc_avg_price_for_year())
