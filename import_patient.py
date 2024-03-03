import patient

def main():
    def patient_info():
        name = input('Введите имя: ')
        otchestvo = input('Введите отчество: ')
        familiya = input('Введите фамилию: ')
        adreses = input('Введите адрес: ')
        city = input('Введите Город: ')
        oblasty = input('Введите Область: ')
        po4tovii_index = int(input('Введите почтовый индекс: '))
        phone = int(input('Введите номер телефона: '))
        name_and_sos_phone = name, phone

        obj = patient.Patient(name, adreses, phone, name_and_sos_phone)

        obj.set_names(name, otchestvo, familiya)
        obj.set_adreses(adreses, city, oblasty, po4tovii_index)
        obj.set_name_and_sos_phone(name, phone)

        print('Имя-фамилия-отчество--------')
        print(obj._str_name_info())
        print('Номер----------')
        print(obj._str_phone())
        print('SOS данные-------')
        print(obj._str_sos_name_phone())
        print('Адресса---------')
        print(obj._str_adreces())
    # patient_info()
    def procedur():
        result = []
        result_sum = []
        for _ in range(3):
            procedur_name = input('Введите название процедуры: ')
            date = input('Введите дату процедуры: ')
            doctor_name = input('Введите имя доктора: ')
            price = int(input('Введите цену: '))

            obj = patient.Procedur(procedur_name, date, doctor_name, price)
            result.append(obj)

        for item in result:
            print( f'{item.get_procedur_name()}\n' + \
                   f'{item.get_date()}\n' + \
                   f'{item.get_doctor_name()}\n' + \
                   f'{item.get_price()}\n'
                   )
            price = obj.get_price()
            result_sum.append(price)
        print(f' Общая сумма всех процедур составляет: {sum(result_sum)}')



    procedur()
if __name__ == '__main__':
    main()