import class_employee

def main():
    name = input('Введите имя: ')
    phone = input('Введите номер: ')

    employee_obj = class_employee.Employee(name, phone)

    nomer_smeni = input('Введите номер смены: ')
    money_for_1_hour = input('Введите почасовую ставку: ')

    productworker_obj = class_employee.ProductionWorker(name, phone, nomer_smeni, money_for_1_hour)

    print('Вот введённые вами данные: ')
    print(employee_obj.__str__())
    print(productworker_obj.__str__())


if __name__ == '__main__':
    main()