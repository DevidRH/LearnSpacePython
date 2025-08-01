#ANCHOR - Character Class EX4
"""
Write a Python function to find all character combinations starting with 'a' or 'e' in a given string.

Example

text = "The following example creates a list with 50 elements. All elements are then added to the list when the list is created."
start_ae(text)
Output

['example', 'eates', 'elements', 'elements', 'are', 'en', 'added', 'en', 'eated']

"""

import re

v_text = "The following example creates a list with 50 elements. All elements are then added to the list when the list is created."

def start_ae(p_text):
  regex_pattern = re.compile(r'[ae]\w+')
  x = regex_pattern.findall(p_text)
  return x

print(start_ae(v_text))