class Pet:

    def __init__(self, name, animal_type, age) -> None:
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def get_animal_type(self):
        return self.__animal_type
    
    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age
    
    def __str__(self) -> str:
        return f'Имя: {self.__name}\n' + \
               f'Тип животного: {self.__animal_type}\n' + \
               f'Возраст: {self.__age}'