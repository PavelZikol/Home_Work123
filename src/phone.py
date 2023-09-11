from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity,num_sim):
        self.__init__(name,price,quantity)
        self.num_sim = num_sim
