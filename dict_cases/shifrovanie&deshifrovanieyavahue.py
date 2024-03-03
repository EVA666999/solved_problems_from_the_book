import pickle
#1/зашифровать то что в file.txt во второй файл file.dat
my_dict = {
    'А': '%', 'а': '9', 'Б': '@', 'б': '#', 'В': '&',
    'в': '*', 'Г': '$', 'г': '!', 'Д': '^', 'д': '~',
    'Е': '(', 'е': ')', 'Ё': '[', 'ё': ']', 'Ж': '{',
    'ж': '}', 'З': '|', 'з': '☯', 'И': '<', 'и': '>',
    'Й': '`', 'й': '+', 'К': '=', 'к': '☀', 'Л': '_',
    'л': '/', 'М': ':', 'м': ';', 'Н': '.', 'н': ',',
    'О': '!', 'о': '?', 'П': '/', 'п': '\\', 'Р': '↓',
    'р': '♨', 'С': '3', 'с': '5', 'Т': '7', 'т': '1',
    'У': '0', 'у': '8', 'Ф': '4', 'ф': '2', 'Х': '6',
    'х': '!', 'Ц': '#', 'ц': '@', 'Ч': '$', 'ч': '%',
    'Ш': '^', 'ш': '&', 'Щ': '*', 'щ': '(', 'Ъ': ')',
    'ъ': 'Ⓠ', 'Ы': 'Ⓢ', 'ы': '✩', 'Ь': '❥', 'ь': '|',
    'Э': '❤', 'э': ':', 'Ю': ';', 'ю': ',', 'Я': '.',
    'я': '-', ' ': ' ' 
}


def write():
    file = open('file.txt', 'w', encoding='utf-8')
    file.write('я пися розы')
    file.close()

print(write())

def read():
    file = open('file.txt', 'r', encoding='utf-8')
    line = file.readline()
    file.close()
    return ''.join(line)

print(read())

def shifr():
    text = read()
    result = ''
    for i in text:
        if i in my_dict.keys():
            result += my_dict[i]
    return result

print(shifr())

def unshifr():
    unsh = shifr()
    print(len(unsh))
    result = ''
    for i in unsh:
        for k, v in my_dict.items():
            if i == v:
                result += k
    return result

print(unshifr())