import pickle

FOUND = 1
ADD = 2
CHANGE = 3
DEL = 4
QUIT = 0
names = ['ian', 'anna', 'olya', 'myauu']
mail = ['a1', 'b2', 'c3', 'g4']
my_dict = {k:v for (k,v) in zip(names, mail)}




def main():
    def found():
        ask = input('Введите имя человека: ')
        while ask != 'н':
            return my_dict.get(ask, 'Такого имени нет!')
        file = open('pickle_file.dat', 'wb')
        pickle.dump(my_dict, file)
        file = open('pickle_file.dat', 'rb')
        print(pickle.load(file))
        print('Программа завершена!')
        quit()
        
    def add():
        key = input('Введите имя человека что бы добавить его в словарь: ')
        while key != 'н':
            if key not in my_dict:
                value = input('Введите email человека: ')
                my_dict[key] = value
            else:
                print('Имя уже существует!')
            return my_dict
        file = open('pickle_file.dat', 'wb')
        pickle.dump(my_dict, file)
        file = open('pickle_file.dat', 'rb')
        print('Программа завершена!')
        print(pickle.load(file))
        quit()

    def change():
        key = input('Ведите имя человека: ')
        while key != 'н':
            if key in my_dict:
                value = input('Измените адресс почты для чела: ')
                my_dict[key] = value
            else:
                print('Такого имени нет')
            return my_dict
        file = open('pickle_file.dat', 'wb')
        pickle.dump(my_dict, file)
        file = open('pickle_file.dat', 'rb')
        print('Программа завершена!')
        print(pickle.load(file))
        quit()

    def delite():
        key = input('Введите имя кототорое хотите удалить из словаря! ')
        while key != 'н':
            if key in my_dict:
                del my_dict[key]
            else:
                print('Такого имени нет!')
            return my_dict
        file = open('pickle_file.dat', 'wb')
        pickle.dump(my_dict, file)
        file = open('pickle_file.dat', 'rb')
        print('Программа завершена!')
        print(pickle.load(file))
        quit()
        




    ask = int(input('Введите номер из меню: '))
    while ask != QUIT:
        if FOUND == ask:
            print(found())
        elif ADD == ask:
            print(add())
        elif CHANGE == ask:
            print(change())
        elif DEL == ask:
            print(delite())

if __name__ == '__main__':
    main()

