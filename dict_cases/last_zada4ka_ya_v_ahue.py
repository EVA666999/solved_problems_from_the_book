import re



def read_file():
    file = open('text_file.txt', 'r', encoding='utf-8')
    line = file.readline().rstrip('\n')
    result = []
    split_string = ''
    my_dict = {}
    while line != '':
        result.append(line)
        split_string += line
        line = file.readline().rstrip('\n')
    file.close()
    for word in result:
        index = result.index(word)
        my_dict[word] =  index + 1
    word_count = {}
    for line, index in my_dict.items():
        words = line.split()
        for word in words:
            word_count[word] = word_count.get(word, []) + [index]

    return word_count
print(read_file())