# py-roman (not to be confused with Pyro-Man)

Module to convert Roman numerals to integers and vice versa


```
>>> import roman_numerals
>>> roman_numerals.integer_to_numeral(25)
>>> roman_numerals.integer_to_numeral(35)
'XXXV'
>>> roman_numerals.integer_to_numeral(228)
'CCXXVIII'
>>> roman_numerals.numeral_to_integer('CCXXVIII')
228
>>> roman_numerals.numeral_to_integer('CCXXVI')
226
```


This simple module is a practice in using functional programming patterns in Python.
Each function is documented with readable doctests.
Tests can be run from command line with `python -m doctest roman_numerals.py` - no output means the tests were successful.
