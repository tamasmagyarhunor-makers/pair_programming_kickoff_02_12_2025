from lib.fizzbuzz import *
import pytest

def test_returns_fizz_when_called_with_3():
    """
    returns fizz if called with 3
    """
    actual = fizzbuzz(3)
    expected = 'fizz'

    assert actual == expected

def test_returns_buzz_when_called_with_5():
    """
    returns buzz if called with 5
    """
    actual = fizzbuzz(5)
    expected = 'buzz'

    assert actual == expected

def test_returns_fizzbuzz_when_called_with_15():
    """
    returns fizzbuzz if called with 15
    """
    actual = fizzbuzz(15)
    expected = 'fizzbuzz'

    assert actual == expected

def test_returns_number_if_called_with_8():
    """
    returns number if called with 8, or any number not divisible by either
    """
    actual = fizzbuzz(8)
    expected = 8

    assert actual == expected

def test_raise_error_when_input_not_int():
    """
    raise Error when input not int
    """
    with pytest.raises(TypeError) as error:
        fizzbuzz("test")
    actual = error.value
    expected = "Input can only be integer!"

    assert str(actual) == expected