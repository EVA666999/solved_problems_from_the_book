dtc = {'james': 1, 'Anna': 2, 'Джими': 3}
if 'james' in dtc:
    print(dtc['james'])
else:
    print('Такого ключа нету')

dct1 = {'james': 1, 'Anna': 2, 'Джими': 3}
if 'Джими' in dct1:
    k, v = dct1.popitem()
    print(dct1)