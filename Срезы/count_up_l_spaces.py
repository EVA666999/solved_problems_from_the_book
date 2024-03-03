def main():
    file = open('text.txt', 'r', encoding='utf-8')
    line = file.readline().rstrip('\n')
    result = []
    for_upper = ''
    for_lower = ''
    for_spaces = ''
    while line != '':
        result.append(line)
        line = file.readline().rstrip('\n')
    for i in result:
        for j in i:
            if j.isupper():
                for_upper += j
            elif j.islower():
                for_lower += j
            elif j.isspace():
                for_spaces += j
    print(f'Букв в верхнем регистре: {len(for_upper)}, в нижнем: {len(for_lower)}, всего пробелов: {len(for_spaces)}')

if __name__ == '__main__':
    main()
