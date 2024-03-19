class Dog:

    def __init__(self, name) -> None:
        self.__name = name

    def set_name(self, name):
        self.__name == name

    def get_name(self):
        return self.__name
    
class Pooldel(Dog):
    
    def __init__(self, name) -> None:
        super().__init__(name)
