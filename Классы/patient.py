class Patient:

    def __init__(self, names_info, adreses, phone, name_and_sos_phone) -> None:
        self.__names = names_info
        self.__adreses = adreses
        self.__phone = phone
        self.__name_and_sos_phone = name_and_sos_phone

    def set_names(self, names, otchestvo, familiya):
        self.__names = names
        self.__otchestvo = otchestvo
        self.__familiya = familiya

    def get_names(self):
        return self.__names, self.__otchestvo, self.__familiya
    
    def set_adreses(self, adreses, city, oblasty, po4tovii_index):
        self.__adreses = adreses
        self.__city = city
        self.__oblasty = oblasty
        self.__po4tovii_index = po4tovii_index

    def get_adreses(self):
        return self.__adreses, self.__city, self.__oblasty, self.__po4tovii_index
    
    def set_phone(self, phone):
        self.__phone = phone

    def get_phone(self):
        return self.__phone
    
    def set_name_and_sos_phone(self, name, phone):
        self.__name_and_sos_phone = name, phone

    def get_name_and_sos_phone(self):
        return self.__name_and_sos_phone


    def _str_name_info(self) -> str:
        return f'Имя {self.__names}\n' + \
               f'Отчество {self.__otchestvo}\n' + \
               f'Фамилия {self.__familiya}\n'
    
    def _str_phone(self) -> str:
        return   f'Телефон {self.__phone}\n'
    
    def _str_sos_name_phone(self) -> str:
        return   f'Данные для sos {self.__name_and_sos_phone}\n'
    
    def _str_adreces(self) -> str:
        return   f'Адрес: {self.__adreses}\n' + \
                 f'Город: {self.__city}\n' + \
                 f'Область: {self.__oblasty}\n' + \
                 f'Почтовый индекс: {self.__po4tovii_index}\n'
    

class Procedur:

    def __init__(self, procedur_name, date, doctor_name, price) -> None:
        self.__procedur_name = procedur_name
        self.__date = date
        self.__doctor_name= doctor_name
        self.__price = price

    def set_procedur_name(self, proceur_name):
        self.__procedur_name = proceur_name

    def get_procedur_name(self):
        return self.__procedur_name
    
    def set_date(self, date):
        self.__date = date

    def get_date(self):
        return self.__date
    
    def set_doctor_name(self, doctor_name):
        self.__doctor_name = doctor_name

    def get_doctor_name(self):
        return self.__doctor_name
    
    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price
    
    def __str__(self) -> str:
        return f'Название процедуры: {self.__procedur_name}\n' + \
               f'Дата: {self.__date}\n' + \
               f'Имя доктора: {self.__doctor_name}\n' +\
               f'Цена: {self.__price}\n'