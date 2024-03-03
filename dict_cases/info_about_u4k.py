def info():
    my_dict = {}
    nobers_of_course = ['CS101', 'CS102', 'CS103', 'CS104', 'CS105']
    cabinet = [[3004, 'Хайнс', '8:00'], [4501, 'Альвардо', '9:00']]
    my_dict = {k:v for (k, v) in zip(nobers_of_course, cabinet)} # крутатенььььььььььььььььььььььььььь
    ask = input('Введите номер: ')
    return my_dict.get(ask.upper(), 'Такого номера нету')
print(info())

