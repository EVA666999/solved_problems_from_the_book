def count():
    file = open('file.txt', 'r', encoding='utf-8')
    line = file.read()
    result = ''
    result += line
    result = result.split()
    key = set(result)
    rez = dict.fromkeys(key, 0)
    for key in result:
        rez[key] += 1
    return rez
    

print(count())