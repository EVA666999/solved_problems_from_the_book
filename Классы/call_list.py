import cellphonel

def main():

    phones = make_list()
    print('Вот введённые вами данные!')
    dislplay_list(phones)

def make_list():
    phone_list = []
    for _ in range(2):
        man = input('Введите производителя')
        model = input('Введите модель')
        price = int(input('Введите цену'))
        print()

        phon = cellphonel.Chellphone(man, model, price)
        phone_list.append(phon)
    return phone_list

def dislplay_list(phone_list):
    for item in phone_list:
        print(item.get_manufact())
        print(item.get_model())
        print(item.get_retail_price())


if __name__ == '__main__':
    main()
    