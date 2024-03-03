def unique_words_in_2_files(name='file.txt'):
    file = open(name, 'r', encoding='utf-8')
    line = file.read()
    result = ''
    result += line
    result = result.split()
    unique_words = set(result)
    return unique_words


def second_file():
    return unique_words_in_2_files(name='file1.txt')


def unique_words_for_2_files():
    file1 = unique_words_in_2_files()
    file2 = second_file()
    result = file1 | file2
    return result


def all_words_in_both_files():
    file1 = open('file.txt', 'r', encoding='utf-8')
    file2 = open('file1.txt', 'r', encoding='utf-8')
    line1 = file1.read()
    line2 = file2.read()
    result = ''
    result += line1 + '\n' + line2
    return result

def diference():
    file1 = open('file.txt', 'r', encoding='utf-8')
    file2 = open('file1.txt', 'r', encoding='utf-8')
    line1 = file1.read()
    line2 = file2.read()
    result1 = ''
    result1 += line1
    result2 = ''
    result2 += line2
    set1 = set(result1.split())
    set2 = set(result2.split())
    return set1.difference(set2)

def symmetric_difference():
    file1 = open('file.txt', 'r', encoding='utf-8')
    file2 = open('file1.txt', 'r', encoding='utf-8')
    line1 = file1.read()
    line2 = file2.read()
    result1 = ''
    result1 += line1
    result2 = ''
    result2 += line2
    set1 = set(result1.split())
    set2 = set(result2.split())
    return set1.symmetric_difference(set2)


print(symmetric_difference())