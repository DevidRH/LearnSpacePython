#ANCHOR - Find Three Consecutive Digits
"""
Implement a function which takes a string as a parameter to find out whether there is three consecutive digits or not. 
If there is three consecutive digits, the function will return first occurence otherwise 'Not found'.

Example

text = 'My phone number is: 234-456-8765'
find_three_con(text)
Output

234

"""

import re

text = 'My phone number is: 234-456-8765'

def find_three_front(p_text):
  v_search = re.search(r'\d\d\d', p_text)     #NOTE - Tells Python this is a raw string, so \d means a regex digit
  
  if v_search == None:
    return 'Not Founc'
  else:
    return v_search.group()     #NOTE - The .group() method is used to return the actual matched string from a regex search.

print(find_three_front(text))