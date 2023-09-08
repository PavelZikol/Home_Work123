"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


def test_Item():
    """Тестирование полей класса Item"""
    item1 = Item("Плазма", 200000, 2)
    assert item1.name == "Плазма"
    assert item1.price == 200000
    assert item1.quantity == 2
    item1.name = "Утюг"
    assert item1.name == "Утюг"
    item1.name = "Утюг крутой супер"
    assert item1.name == "Утюг круто"


def test_calculate_total_price():
    """Тестирование метода расчета количества товара"""
    item1 = Item("Смартфон", 5, 10)
    item2 = Item("Ноутбук", 2, 50000)
    assert item1.calculate_total_price() == 50
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    """Тестирование метода применения скидки возвращающий None"""
    item1 = Item("Наушники", 15000, 80)
    assert item1.apply_discount() is None


def test_Item_string_to_number():
    assert Item.string_to_number("6") == 6
    assert Item.string_to_number("10.4") == 10