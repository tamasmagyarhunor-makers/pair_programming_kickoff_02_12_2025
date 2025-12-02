# Create a fizzbuzz function
- function signature
- edge cases
- examples of behaviour

### function/method signature
```python
"""
Parameters:
  - takes an int, number 
Returns:
  - string/int, e.g. 'fizz' or 8
Side effects:
  - 
Notes/Edge cases
  - fizz if divisible by 3
  - buzz if divisible by 5
  - fizzbuzz if divisible by 15
  - return number if neither
"""
def fizzbuzz(number):
    pass

```

### examples
```python
from lib.fizzbuzz import fizzbuzz

"""
returns fizz if called with 3
"""
actual = fizzbuzz(3)
expected = 'fizz'

assert actual == expected

"""
returns buzz if called with 5
"""
actual = fizzbuzz(5)
expected = 'buzz'

assert actual == expected

"""
returns fizzbuzz if called with 15
"""
actual = fizzbuzz(15)
expected = 'fizzbuzz'

assert actual == expected

"""
returns number if called with 8, or any number not divisible by either
"""
actual = fizzbuzz(8)
expected = 8

assert actual == expected


```
