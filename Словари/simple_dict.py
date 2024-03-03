my_dict = {1: 'Вася', 4: 'мяу'}
my_dict[2] = 'Пися'
my_dict[5] = 'Пиaaaaaaaaaaся'
my_dict[3] = 'удалить'
del my_dict[3]
for key in my_dict:
    print(key)
print(my_dict.get(1, 'Такого значения нет'))
print(my_dict.items())
print(my_dict.keys())
my_dict.pop(11, 'ключ не найден_________')
print(my_dict)
print(my_dict.values())
k, v = my_dict.popitem()
print(my_dict, k, v)
dd = {1: [1, 2 ,3], 2: 'b'}
