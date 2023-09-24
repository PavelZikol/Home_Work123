import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """гетер"""
        return self.__name

    @name.setter
    def name(self, new_name):
        """поменять имя"""
        if 0 < len(new_name) < 10:
            self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls, file):
        """открытие csv и заполнение пусого списка all"""
        cls.all = []
        with open(file) as f:
            reader = csv.DictReader(f)
            for i in reader:
                cls.all.append(cls(i["name"], i["price"], i["quantity"]))

    @staticmethod
    def string_to_number(num):
        """Возврат чисел из строки"""
        return int(float(num))

    def __add__(self, other):
        if isinstance(other, Item):
            return Item(self.quantity + other.quantity)

    def __repr__(self):
        return f"Item({repr(self.__name):str}, {repr(self.price):float}, {repr(self.quantity):int})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            total_sum = self.quantity + other.quantity
            return total_sum
        return f"Sorry, bro)"


