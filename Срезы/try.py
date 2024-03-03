i = 0
a = 0
while i < len(sum_for_m_1993):
    file_sum = [float(x) for x in sum_for_m_1993[i:i+4]]

    if len(file_sum) == 4:
        a += 1
        total = sum(file_sum)
        print(f'Сумма месяца {a} - 1993 года: {file_sum} = {total}')
        
    i += 1