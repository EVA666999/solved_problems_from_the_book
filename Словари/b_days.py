LOOK_UP = 1
ADD = 2
CHANGE = 3
DEL = 4
QUIT = 5
my_dict = {'Ваня': '5/6/1999', 'Саня': '11/11/1333'}
def main():
    def loock_up():
        ask = input('Введите человека чей день рождения хотите найти: ')
        return my_dict.get(ask, 'такого человека нет!')

    def add():
        key = input('Введите имя человека что бы добавить его в словарь: ')
        if key not in my_dict:
            value = input('Введите день рождения человека: ')
            my_dict[key] = value
        else:
            print('Имя уже существует!')
        return my_dict

    def change():
        key = input('Введите имя человека чей день рождения хотите изменить: ')
        if key not in my_dict.keys():
            print('Такого имени нет в словаре')
        else:
            value = input('Введите день рождения: ')
            my_dict[key] = value
        return my_dict


    def delete():
        key = input('Введите имя чей день рождения удалить')
        if key not in my_dict.keys():
            print('Такого имени нет в словаре')
        else:
            del my_dict[key]
        return my_dict
    
    ask = int(input('Какое действие хотите сделать? '))
    while ask != QUIT:
        if LOOK_UP == ask:
            print(loock_up())
        elif ADD == ask:
            print(add())
        elif CHANGE == ask:
            print(change())
        elif DEL == ask:
            print(delete())
        else:
            print('Введите одно из выше упомянутых значений')
        ask = int(input('Какое действие хотите сделать? '))

if __name__ == '__main__':
    main()