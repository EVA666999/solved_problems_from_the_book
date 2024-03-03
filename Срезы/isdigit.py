cg = '1вв'
has_digit = False
for i in cg:
    if i.isdigit():
        has_digit = True
if has_digit:
    print('Цыфра')
else:
    print('Цыфры нет!')