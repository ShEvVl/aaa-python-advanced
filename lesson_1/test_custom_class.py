import pytest
import json
from custom_class import Advert


def test_advert_with_nested_attributes():
    lesson_str = """{
        "title": "python",
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
        }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert lesson_ad.location.address == "город Москва, Лесная, 7"


def test_advert_with_keyword_attribute():
    dog_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs"
        }"""
    dog = json.loads(dog_str)
    dog_ad = Advert(dog)
    assert dog_ad.class_ == "dogs"


def test_advert_negative_price_on_creation():
    lesson_str = '{"title": "python", "price": -1}'
    lesson = json.loads(lesson_str)
    with pytest.raises(ValueError):
        Advert(lesson)


def test_advert_negative_price_on_assignment():
    lesson_str = '{"title": "python", "price": 1}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    with pytest.raises(ValueError):
        lesson_ad.price = -3


def test_advert_default_price():
    lesson_str = '{"title": "python"}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert lesson_ad.price == 0


def test_advert_print():
    advert_str = '{"title": "iPhone X", "price": 100}'
    advert = json.loads(advert_str)
    advert_ad = Advert(advert)
    expected_output = "\033[33m" + "iPhone X | 100 ₽" + "\033[0m"
    assert str(advert_ad) == expected_output
