class Car:

    def __init__(self, year_model, make, speed) -> None:
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    def set_year_model(self, year_model):
        self.__year_model = year_model

    def get_year_model(self):
        return self.__year_model
    
    def set_make(self, make):
        self.__make = make

    def get_make(self):
        return self.__make
    
    def set_accelerate(self, speed):
        self.__speed  = speed
        self.__speed += 5
    
    def get_accelerate(self):
        return self.__speed
    
    def set_break_speed(self):
        self.__speed -= 5

    def get_break_speed(self):
        return self.__speed
    
    def str_accelerate(self) -> str:
        return f'Accelerate: {self.__speed}'

    def str_break(self) -> str:
        return f'Break: {self.__speed}'