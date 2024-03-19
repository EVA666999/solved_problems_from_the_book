class Beverage:
    def __init__(self, bev_name) -> None:
        self.__bev_name = bev_name

    def set_bev_name(self, bev_name):
        self.__bev_name == bev_name

    def get_bev_name(self):
        return self.__bev_name


class Cola(Beverage):
    def __init__(self, bev_name='кокакола') -> None:
        super().__init__(bev_name)

    def __str__(self):
        return f'Cola Beverage: {self.get_bev_name()}'

cola = Cola()
print(cola)