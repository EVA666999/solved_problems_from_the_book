import cash_register

def main():
    register = cash_register.Cashregister()  # Создаем объект Cashregister
    result = []
    result_for_price = []

    for _ in range(2):
        description = input('Введите название: ')
        count = int(input('Введите количество: '))
        price = int(input('Введите цену: '))

        obj = cash_register.Retailitem(description, count, price)

        obj.set_description(description)
        obj.set_count(count)
        obj.set_price(price)
        
        result.append(obj)
        result_for_price.append(price)

    print("Введенные товары:")
    for item in result:
        print(f'{item.get_description()}\n' + \
              f'{item.get_count()}\n' + \
              f'{item.get_price()}\n')
        
    def add():
        for item in result:
            register.purchase_item(item)  # Добавляем каждый товар в кассу

    def get_total():
        for item in result_for_price:
            register.get_total(item)
        print(f'Сумма всех покупок: {register._str_total_sum()}\n')

    def show_items():
        for i in result:
            register.show_items(i)
        print(register._str_show_items())

    def clear():
        register.clear()
        print(register._str_clear())

    add()
    get_total()
    show_items()
    clear()
if __name__ == '__main__':
    main()