from src.item import Item

class MixinLan:
    """Инициализация класса Mixin"""
    Language = "EN"

    def __init__(self):
        self.__language = self.Language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """Инициализация метода изменения клавиатуры"""
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"

        return self.language


class Keyboard(Item, MixinLan):
    """Keyboard subclass initializing"""
    pass