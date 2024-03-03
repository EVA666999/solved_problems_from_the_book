def main():
    a = int(input('Введите цыфру для а'))
    b = int(input('Введите цыфру для b'))
    c = a + b
    print(c)
    ask = 'да'
    while ask.lower() != 'н':
        print(c)
        ask = input('Повторить программу? д=да, н=нет')

if __name__ == '__main__':
    main()