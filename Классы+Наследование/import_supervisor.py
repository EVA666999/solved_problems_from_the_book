import shift_supervisor

def main():
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    godovoy_oklad = input('Введите годовой оклад: ')
    godovaya_premiya = input('Введите годовую премию: ')

    obj_supervisor = shift_supervisor.Shifv_supervisor(name, phone, godovoy_oklad, godovaya_premiya)

    print(obj_supervisor.__str__())

if __name__ == '__main__':
    main()