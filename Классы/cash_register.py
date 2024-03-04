class Retailitem:

    def __init__(self, description, count, price) -> None:
        self.__description = description
        self.__count = count
        self.__price = price

    
    def set_description(self, description):
        self.__description = description

    def get_description(self):
        return self.__description
    
    def set_count(self, count):
        self.__count = count

    def get_count(self):
        return self.__count
    
    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price
    
    def __str__(self) -> str:
        return f'Название: {self.__description}\n' + \
               f'Количество: {self.__count}\n' + \
               f'Цена: {self.__price}\n'


class Cashregister:
    def __init__(self):
        self.items = []
        self.total_sum = []
        self.__show_items = []

    def purchase_item(self, retail_item):  # Метод принимает объект Retailname
        self.items.append(retail_item)

    def get_total(self, price):
        self.total_sum.append(price)

    def show_items(self, items):
        self.__show_items.append(items)

    def clear(self):
        self.__show_items.clear()

    def _str_show_items(self) -> str:
        result = "Корзина:\n"
        for item in self.__show_items:
            result += str(item) + "\n"
        return result
    
    def _str_total_sum(self) -> str:
        total_sum = 0
        for i in self.total_sum:
            total_sum += i
        return total_sum
    
    def _str_clear(self):
        self.__show_items.clear()
        return self.__show_items
    