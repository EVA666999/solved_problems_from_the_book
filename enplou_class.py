class Employ:
    
    def __init__(self, name, number, cabinet, dolzhnosti) -> None:
        self.__name = name
        self.__number = number
        self.__cabinet = cabinet
        self.__dolzhnosti = dolzhnosti

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    
    def set_number(self, number):
        self.__number = number

    def get_number(self):
        return self.__number
    
    
    def set_cabinet(self, cabinet):
        self.__cabinet = cabinet

    def get_cabinet(self):
        return self.__cabinet
    
    
    def set_dolzhnosti(self, dolzhnosti):
        self.__dolzhnosti = dolzhnosti

    def get_dolzhnosti(self):
        return self.__dolzhnosti
    
    def __str__(self) -> str:
        return f'Имя: {self.__name}\n' + \
               f'номер: {self.__number}\n' + \
               f'кабинет: {self.__cabinet}\n' + \
               f'Должность: {self.__dolzhnosti}'