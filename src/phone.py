class Phone(Item):
    """Phone subclass initializing"""

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """Repr method initializing"""
        return (f"{self.__class__.__name__}('{self.name}', {self.price}, "
                f"{self.quantity}, {self.number_of_sim})")

    @property
    def number_of_sim(self):
        """numbers_of_sim getter"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """numbers_of_sim setter: if value <= 0 or value is not int - Error"""
        if value <= 0 or not isinstance(value, int):
            print(f"ValueError: Количество физических SIM-карт "
                  f"должно быть целым числом больше нуля.")
        else:
            self.__number_of_sim = value