import enplou_class
import pickle

def main():

    result = []

    def make_list():
        for _ in range(3):
            name = input('Введите имя: ')
            number = input('Введите телефон: ')
            cabinet = input('Введите кабинет: ')
            dolzhnosti = input('Введите должность: ')

            obj = enplou_class.Employ(name, number, cabinet, dolzhnosti)

            obj.set_name(name)
            obj.set_number(number)
            obj.set_cabinet(cabinet)
            obj.set_dolzhnosti(dolzhnosti)
            result.append(obj)
        
        return result
        
    def display(result):
        for i in result:
            print(f'{i.get_name()}\n' + \
                  f'{i.get_number()}\n' + \
                  f'{i.get_cabinet()}\n' + \
                  f'{i.get_dolzhnosti()}\n')
            
    def create_dict():
        k_for_dict = []
        v_for_dict = []
        my_dict = {}
        for item in result:
            k_for_dict.append(item.get_number())
            v_for_dict.append(item.get_name())
            v_for_dict.append(item.get_cabinet())
            v_for_dict.append(item.get_dolzhnosti())
            my_dict[item.get_number()] = [item.get_name(), item.get_cabinet(), item.get_dolzhnosti()]
        return my_dict


    result = make_list()
    print('Вот ваши данные!\n')
    display(result)
    print(create_dict())

    def menu():
        FILENAME = 'save_dict_data.dat'
        QUIT = 0
        FOUND = 1
        ADD = 2
        CHANFE_VALUES = 3
        DEL = 4

        def open_file_and_read():
            file = open(FILENAME, 'rb')
            end = False
            while not end:
                try:
                    my_dict = pickle.load(file)
                except EOFError:
                    end = True
            file.close()
            return my_dict
        
        try:
            my_dict = open_file_and_read()
        except FileNotFoundError:
            print(f'Файла {FILENAME} не существует!\n')
            print('Создаю новый словарь')
            my_dict = create_dict()
            print('Словарь создан!')

        def found():
            ask = input('Введите имя сотрудкика: ')
            for k, v in my_dict.items():
                if ask in v:
                    return (k, v)
                
        def add():
            name = input('Введите имя: ')
            number = input('Введите телефон: ')
            cabinet = input('Введите кабинет: ')
            dolzhnosti = input('Введите должность: ')
            if number not in my_dict.keys():
                my_dict[number] = [name, cabinet, dolzhnosti]
                return my_dict
            else:
                return 'Пользователь с таким индентификационным номером уже существует!'
            
        
        def change():
            ask = input('Введите номер сотрудника чьи данные хотите изменить: ')
            if ask in my_dict.keys():
                name = input('Введите имя: ')
                dolzhnosti = input('Введите должность: ')
                cabinet = input('Введите кабинет: ')
                my_dict[ask]  = [name, dolzhnosti, cabinet]
                return my_dict
            else:
                return 'Пользователь с таким номером не найден!'
            
        def delete():
            ask = input('Введите ключ сотрудника что бы удалить сотрудника: ')
            if ask in my_dict.keys():
                del my_dict[ask]
                return my_dict
            else:
                return 'Такого клдюча нет!'
            
        def save_data():
            file = open(FILENAME, 'wb')
            pickle.dump(my_dict, file)
            file.close()
            return f'Данные записаны в файл {FILENAME}'

        ask = int(input('Выберите пункт из меню: '))
        while ask != QUIT:
            if FOUND == ask:
                print(found())
                ask = int(input('Выберите пункт из меню: '))
            elif ADD == ask:
                print(add())
                ask = int(input('Выберите пункт из меню: '))
            elif CHANFE_VALUES == ask:
                print(change())
                ask = int(input('Выберите пункт из меню: '))
            elif DEL == ask:
                print(delete())
                ask = int(input('Выберите пункт из меню: '))

        print(save_data())
        open_file_and_read()

    menu()

if __name__ == '__main__':
    main()
