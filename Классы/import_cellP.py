import cellphonel

def main():
    manufact = input('Введите название телефона')
    model = input('Введите модель телефона')
    price = int(input('Введите цену'))
    phone = cellphonel.Chellphone(manufact, model, price)
    phone.set_manufact(manufact)
    phone.set_model(model)
    phone.set_retail_price(price)
    print(phone.get_manufact())
    print(phone.get_model())
    print(phone.get_retail_price())


if __name__ == '__main__':
    main()