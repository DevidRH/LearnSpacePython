#ANCHOR - is Decimal

"""
Implement a function which takes a parameter and checks for a decimal with a precision of 1 or 2. 
If the number is decimal with a precision of 1 or 2 it will return True otherwise False.

Example

is_decimal('123.11')
is_decimal('123.1')
is_decimal('123.123')
Output

True
True
False

"""

import re

def is_decimal(p_number):
  regex_pattern = re.compile(r'\d+[.]\d{1,2}$')     #NOTE - or re.compile(r'^[0-9]+\.[0-9]{1,2}$')
  x = regex_pattern.search(p_number)
  return bool(x)

print(is_decimal('123.11'))
print(is_decimal('123.1'))
print(is_decimal('123.123'))