def weather(string):
    if not isinstance(string, str):
        raise TypeError('Input must be a string!')
    if string == 'sunny':
        return 'Take the sunglasses!'
    if string == 'rainy':
        return 'Take the raincoat!'
    return 'Weather not recognised'