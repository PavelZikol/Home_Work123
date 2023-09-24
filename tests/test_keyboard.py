from src.keyboard import Keyboard


def test_Keyboard():
    """Class Keyboard testing"""
    kb = Keyboard("Razer Anansi", 20, 2)
    assert kb.name == "Razer Anansi"
    assert kb.price == 20
    assert kb.quantity == 2
    assert kb.language == "EN"
    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang()
    assert kb.language == "EN"