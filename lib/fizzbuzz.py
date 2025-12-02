def fizzbuzz(number):
    if type(number) != int:
        raise TypeError("Input can only be integer!")
    if number % 15 == 0:
        return 'fizzbuzz'
    if number % 3 == 0:
        return 'fizz'
    if number % 5 == 0:
        return 'buzz'
      
    return number