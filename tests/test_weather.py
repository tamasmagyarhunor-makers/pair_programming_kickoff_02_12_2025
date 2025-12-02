
def test_returns_take_the_sunglasses_when_called_with_sunny():
    """
    Returns 'Take the sunglasses!' when called with 'sunny'
    """
    actual = weather('sunny')
    expected = 'Take the sunglasses!'

    assert actual == expected