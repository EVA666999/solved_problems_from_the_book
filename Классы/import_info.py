import info_class
def main():

    def my_info():
        name = input('Введите ваше имя: ')
        adress = input('Введите ваш адресс: ')
        age = int(input('Введите ваш возраст'))
        phone = int(input('Введите ваш телефон'))

        obj = info_class.Information(name, adress, age, phone)

        obj.set_name(name)
        obj.set_adress(adress)
        obj.set_age(age)
        obj.set_phone(phone)

        return f'{obj.str_my_info()}'
        
    def friend_info():
        for _ in range(2):
            name = input('Введите имя друга: ')
            adress = input('Введите адресс друга: ')
            age = int(input('Введите возраст друга: '))
            phone = int(input('Введите телефон друга'))

            obj = info_class.Information(name, adress, age, phone)

            obj.set_name(name)
            obj.set_adress(adress)
            obj.set_age(age)
            obj.set_phone(phone)

            print(f'{obj.str_frend_info()}')


    print(my_info())
    print(friend_info())

if __name__ == '__main__':
    main()
