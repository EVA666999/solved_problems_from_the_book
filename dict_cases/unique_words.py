def write():
    file = open('file.txt', 'r', encoding='utf-8')
    line = file.read()
    result = ''
    result += line
    unique_words = ' '.join(set(result.split()))
    file.close()
    return unique_words

print(write())