import class_employee

class Shifv_supervisor(class_employee.Employee):
    def __init__(self, name, phone, godovoy_oklad, godovaya_premiya) -> None:
        super().__init__(name, phone)
        self.__godovoy_oklad = godovoy_oklad
        self.__godovaya_premiya = godovaya_premiya

    def set_godovoy_oklad(self, godovoy_oklad):
        self.__godovoy_oklad = godovoy_oklad

    def get_godovoy_oklad(self):
        return self.__godovoy_oklad
    
    def set_godovaya_premiya(self, godovaya_premiya):
        self.__godovaya_premiya = godovaya_premiya

    def get_godovaya_premiya(self):
        return self.__godovaya_premiya
    
    def __str__(self) -> str:
        return f'Имя: {self.get_name()}\n' + \
               f'Телефон: {self.get_phone()}\n' + \
               f'Годовой оклад: {self.__godovoy_oklad}\n' + \
               f'Премия: {self.__godovaya_premiya}'   