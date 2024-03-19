import class_person

def main():
    name = input('Введите имя: ')
    adres = input('Введите адресс: ')
    phone = input('Введите телефог: ')
    client_number = input('Введите номер клиеннта: ')
    rassilka_bool = int(input('Согласие на рассылку 1-да 2-нет'))

    costumer_obj = class_person.Costumer(name, adres, phone, client_number, rassilka_bool)

    print(costumer_obj.__str__())

if __name__ == '__main__':
    main()