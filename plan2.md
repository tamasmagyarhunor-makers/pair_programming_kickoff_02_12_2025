# A function that tells you to wear sunglasses or raincoat
- function signature
- edge cases
- examples of behaviour

### function/method signature
```python
"""
Parameters:
  - string, string (eg. 'rainy')
Returns:
  - string
Side effects:
  - 
Notes/Edge cases
  - raises TypeError if not string passed in.
  - if input is not 'sunny' or 'rainy' return 'Weather not recognised'
"""
def weather(string):
    pass

```

### examples
```python
from lib.weather import weather
import pytest

"""
Returns 'Take the sunglasses!' when called with 'sunny'
"""
actual = weather('sunny')
expected = 'Take the sunglasses!'

assert actual == expected

"""
Returns 'Take the raincoat!' when called with 'rainy'
"""
actual = weather('rainy')
expected = 'Take the raincoat!'

assert actual == expected

"""
Returns 'Weather not recognised' when called with neither 'rainy' or 'sunny'
"""
actual = weather('muddy')
expected = 'Weather not recognised'

assert actual == expected

"""
Raises TypeError when called with not string
"""
with pytest.raises(TypeError) as e:
  actual = weather('muddy')

actual = e.value
expected = 'Weather not recognised'

assert str(actual) == expected

```
