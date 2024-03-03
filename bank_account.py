class Bank:
    
    def __init__(self, real_schet, zberigatelnii_schet, tacke_cash) -> None:
        self.__real_schet = real_schet
        self.__zberigatelnii_schet = zberigatelnii_schet
        self.__tacke_cash = tacke_cash

    def set_real_schet(self, real_schet, S, G, D, V):
        self.__real_schet = real_schet
        self.__real_schet_with_percent = self.__real_schet + (S * G * D / V)
    
    def get_real_schet(self):
        return self.__real_schet, self.__real_schet_with_percent

    def set_zberigatelnii_schet(self, amount, S, G, D, V) :
        self.__zberigatelnii_schet = self.__real_schet + amount
        self.__schet_with_percent = self.__zberigatelnii_schet + (S * G * D / V)
    
    def get_zberigatelnii_schet(self):
        return self.__zberigatelnii_schet, self.__schet_with_percent
    
    def set_tacke_cash(self, amount, S, G, D, V):
        self.__tacke_cash = self.__zberigatelnii_schet - amount
        self.__tache_cash_with_percent = self.__tacke_cash + (S * G * D / V)
    
    def get_tacke_cash(self):
        return self.__tacke_cash, self.__tache_cash_with_percent
    
    
    def __str__(self) -> str:
        return f'Реальный счёт: {self.__real_schet}\n' + \
               f'Реальный счёт с процентной ставкой: {self.__real_schet_with_percent}\n' + \
               f'Счёт с пополнением: {self.__zberigatelnii_schet} и счёт с процентом {self.__schet_with_percent}\n' + \
               f'Счёт после снятия: {self.__tacke_cash}\n' + \
               f'Счёт с процентом после снятия: {self.__tacke_cash} и с процентами {self.__tache_cash_with_percent}\n'
    # Сделать Счёт с процентом после снятия!
                
