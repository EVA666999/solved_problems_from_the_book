def main():
    file = open('text.txt', 'r', encoding='utf-8')
    line = file.readline().rstrip('\n')
    result = []
    total = 0
    while line != '':
        result.append(line)
        line = file.readline().rstrip('\n')
        total += 1
    result_for_len = 0
    for i in result:
        result_for_len += len(i)
    a = result_for_len / total
    print(f'{a}')
    file.close()


if __name__ == '__main__':
    main()
