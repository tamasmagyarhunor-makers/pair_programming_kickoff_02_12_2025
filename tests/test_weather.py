from lib.weather import *
import pytest


def test_returns_take_the_sunglasses_when_called_with_sunny():
    """
    Returns 'Take the sunglasses!' when called with 'sunny'
    """
    actual = weather('sunny')
    expected = 'Take the sunglasses!'

    assert actual == expected

def test_returns_take_the_raincoat_when_called_with_rainy():
    """
    Returns 'Take the raincoat!' when called with 'rainy'
    """
    actual = weather('rainy')
    expected = 'Take the raincoat!'

    assert actual == expected

def test_returns_weather_not_recognised_when_not_rainy_or_sunny():
    """
    Returns 'Weather not recognised' when called with neither 'rainy' or 'sunny'
    """
    actual = weather('muddy')
    expected = 'Weather not recognised'

    assert actual == expected

def test_raises_typeerror_when_called_with_not_string():
    """
    Raises TypeError when called with not string
    """
    with pytest.raises(TypeError) as e:
        actual = weather(2)

    actual = e.value
    expected = 'Input must be a string!'

    assert str(actual) == expected