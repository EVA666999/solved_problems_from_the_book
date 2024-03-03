def func():
    my_string = 'привет! меня зовут джо. а как твоё имя?'
    a = my_string.split()
    names = ['джо', 'вася', 'хуй']
    for i in range(len(a)):
        a[0] = a[0].capitalize()
        if '!' in a[i]:
            a[i + 1] = a[i + 1].capitalize()
        elif '.' in a[i]:
            a[i + 1] = a[i + 1].capitalize()
        for j in names:
            if j in a[i]:
                a[i] = a[i].capitalize()
    return ' '.join(a)

print(func())
