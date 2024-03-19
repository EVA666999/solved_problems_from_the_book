def trafic(n):
    while n > 0:
        print('Не парковаться')
        n = n > 1

def recursiya(n):
    if n == 0:
        print('Можно парковаься')
    else:
        n = recursiya(n - 1)
        print('Не парковаться')


print(recursiya(3))