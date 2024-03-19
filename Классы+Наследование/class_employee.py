class Employee:
    def __init__(self, name, phone) -> None:
        self.__name = name
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_phone(self, phone):
        self.__phone = phone

    def get_phone(self):
        return self.__phone
    
    def __str__(self) -> str:
        return f'Имя: {self.__name}\n' + \
               f'Номер: {self.__phone}'
    
class ProductionWorker(Employee):
    def __init__(self, name, phone, nomer_smeni, money_for_1_hour) -> None:
        super().__init__(name, phone)
        self.__nomer_smeni = nomer_smeni
        self.__money_for_1_hour = money_for_1_hour

    def set_nomer_smeni(self, nomer_smeni):
        self.__nomer_smeni = nomer_smeni

    def get_nomer_smeni(self):
        return self.__nomer_smeni
    
    def set_money_for_1_hour(self, money_for_1_hour):
        self.__money_for_1_hour = money_for_1_hour

    def get_money_for_1_hour(self):
        return self.__money_for_1_hour
    
    def __str__(self) -> str:
        return f'Номер смены: {self.__nomer_smeni}\n' + \
               f'Почасовая оплата: {self.__money_for_1_hour}'