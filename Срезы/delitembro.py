my_string = 'проспал почти всю ночь'
split_my_strimg = my_string.split()
result = []
for i in split_my_strimg:
    first_word = i[0]
    i = i[:0] +  i[1:]
    result.append(i + first_word + 'ки')
print(' '.join(result))