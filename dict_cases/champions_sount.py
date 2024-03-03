def champions_count():
    file = open('champions.txt', 'r', encoding='utf-8')
    line = file.readline().rstrip('\n')
    result = []
    while line != '':
        result.append(line)
        line = file.readline().rstrip('\n')
    file.close()
    rez1 = {k:v for (k, v) in zip([i for i in range(1903, 2010)], result)}
    for i in result:
        if i == 'Мировая серия, не сыгранная в 1994 году' or i == 'Мировая серия , не сыгранная в 1904 году':
            result.remove(i) 
    key = set(result)
    rez = dict.fromkeys(key, 0)
    for key in result:
        rez[key] += 1
    ask = int(input('Введите год: '))
    if ask < 1903 or ask > 2009:
        ask = int(input('Введите гов в диапазоне 1903-2009: '))
    lol = rez1.get(ask)
    return lol, rez.get(lol)

print(champions_count())



# key = set(result)
# rez = dict.fromkeys(key, 0)
# for key in result:
# rez[key] += 1
# return rez
#{1903: 'Аризона Даймондбэкс'}