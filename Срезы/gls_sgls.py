glass = 'abc'
sogl = 'dfg'


def glasnie():
    my_str = 'kuj8iua'
    count = 0
    for i in glass:
        if i in my_str:
            count += 1
    return f'Количество глассных букв в строке {count}'


def soglasnie():
    my_str = 'kuj8iuaf'
    count = 0
    for i in sogl:
        if i in my_str:
            count += 1
    return f'Количество согласных букв в строке {count}'


print(glasnie(), soglasnie())