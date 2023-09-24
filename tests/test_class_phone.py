import pytest
from src.phone import Phone


def test_Phone():
    """Тестирование поля кол-ва сим карт класса Phone"""
    phone = Phone("Смартфон", 4000, 404, 2)
    assert phone.number_of_sim == 2


def test_repr():
    """Тестирование repr"""
    phone = Phone("Смартфон", 4000, 404, 3)
    assert repr(phone) == "Phone('Смартфон', 4000, 404, 3)"


def test_setter():
    """Тестирование сеттера"""
    phone = Phone("Смартфон", 404, 13, 3)
    phone.number_of_sim = 2
    assert phone.number_of_sim == 2
    phone.number_of_sim = 0
    assert phone.number_of_sim == 2