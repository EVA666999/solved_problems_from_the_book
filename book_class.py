class Book:

    def __init__(self, zagolovok, author_name, izdatel_name) -> None:
        self.__zagolovok = zagolovok
        self.__author_name = author_name
        self.__izdatel_name = izdatel_name

    def set_zagolovok(self, zagolovok):
        self.__zagolovok = zagolovok

    def set_author_name(self, author_name):
        self.__author_name = author_name
        
    def set_izdatel_name(self, izdatel_name):
        self.__izdatel_name = izdatel_name

    def get_zagolovok(self):
        return self.__zagolovok
    
    def get_author_name(self):
        return self.__author_name
    
    def get_izdatel_name(self):
        return self.__izdatel_name

    def __str__(self) -> str:
        return f'Заголовок: {self.__zagolovok}\n' + \
               f'Имя автора: {self.__author_name}\n' + \
               f'Имя издателя: {self.__izdatel_name}'