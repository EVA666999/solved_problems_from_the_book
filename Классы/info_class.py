class Information:

    def __init__(self, name, adress, age, phone) -> None:
        self.__name = name
        self.__adress = adress
        self.__phone = phone
        self.__age = age

    def set_name(self, name):
        self.__name = name
        self.__friend_name = name

    def get_name(self):
        return self.__name

    def get_friebd_name(self):
        return self.__friend_name
    
    def set_adress(self, adress):
        self.__adress = adress

    def get_adress(self):
        return self.__adress
    
    def set_age(self, age):
        self.__age = age

    def get_agee(self):
        return self.__age
    
    def set_phone(self, phone):
        self.__phone= phone

    def get_phone(self):
        return self.__phone
    
    def str_my_info(self) -> str:
        return f'Ваше имя: {self.__name}\n' + \
               f'Ваш адресс: {self.__adress}\n' + \
               f'Ваш Возраст: {self.__age}\n' + \
               f'Ваш номер:  {self.__phone}\n'

    def str_frend_info(self) -> str:
        return f'Имя друга: {self.__name}\n' + \
               f'Адресс друга: {self.__adress}\n' + \
               f'Возраст друга: {self.__age}\n' + \
               f'Номер друга:  {self.__phone}\n'
