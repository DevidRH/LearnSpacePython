#ANCHOR - Regex Pattern EX7
"""
Write a Python function to match a string that has a 'c' or 'C' followed by anything, ending in 'e' or 'E'. 
If match is found it will return the list of matches.

Example Input

text = 'I come to CTRE every year'
text_match(text)
Example Output

['come', 'CTRE']

"""

import re

text = 'I come to CTRE every year'

def text_match(p_text):
  regex_pattern = re.compile(r'^c+')
  text_list = p_text.split()
  
  for word in text_list:
    x = regex_pattern.findall(p_text)
  
  return x

print(text_match(text))