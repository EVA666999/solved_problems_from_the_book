class Person:

    def __init__(self, name, adres, phone) -> None:
        self.__name = name
        self.__adres = adres
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_adres(self, adres):
        self.__adres = adres

    def get_adres(self):
        return self.__adres

    def set_phone(self, phone):
        self.__phone= phone

    def get_phone(self):
        return self.__phone
    
class Costumer(Person):

    def __init__(self, name, adres, phone, client_number, rassilka_bool) -> None:
        super().__init__(name, adres, phone)
        self.__client_number = client_number
        self.__rassilka_bool = rassilka_bool

    def set_client_number(self, client_number):
        self.__client_number = client_number

    def get_client_number(self):
        return self.__client_number
    
    def set_rassilka_bool(self, rassilka_bool):
        self.__rassilka_bool = rassilka_bool

    def get_rassilka_bool(self):
        return self.__rassilka_bool
    
    def __str__(self) -> str:
        return f'Имя {self.get_name()}\n' + \
               f'Адресс: {self.get_adres()}\n' + \
               f'Телефон: {self.get_phone()}\n' + \
               f'Номер клиента: {self.__client_number}\n' + \
               f'Хочет ли рассылку: {self.__rassilka_bool}'