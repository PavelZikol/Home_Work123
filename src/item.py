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
        self.__name = name
        self.price = price
        self.quantity = quantity
        # Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls, file):
        """Class method creating for opening csv file and adding instances to new
        empty all list"""
        cls.all = []
        with open(file) as f:
            reader = csv.DictReader(f)
            for row in reader:
                cls.all.append(cls(row["name"], row["price"], row["quantity"]))

    @staticmethod
    def string_to_number(string_num):
        """Static method creating for returning number from string"""
        if string_num.isdigit():
            return int(string_num)
        return float(string_num) // 1

    @property
    def name(self):
        """Class name getter"""
        return self.__name

    @name.setter
    def name(self, new_name):
        """Class name setter"""
        self.__name = new_name[:10]

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