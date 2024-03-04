import random

class Coin:


    def __init__(self) -> None:
        self.__sideup = 'Орёл'


    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Орёл'
        else:
            self.__sideup = 'Решка'

    def get_sideup(self):
        return self.__sideup
    


def main():

    my_coin = Coin()

    # Бросаем монетку
    my_coin.toss()

    # Получаем результат и выводим в консоль
    print("Результат броска монетки:", my_coin.get_sideup())


if __name__ == '__main__':
    main()