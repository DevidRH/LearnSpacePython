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

text = "I come to CTRE every year"

def text_match(p_text):
  regex_pattern = re.compile(r'^[cC].+[eE]$')     #NOTE - re.compile(r'^c.+e$', re.I) to trigger the capital
  text_list = p_text.split()
  v_result = list()
  for word in text_list:
    x = regex_pattern.findall(word)
    v_result.extend(x)
  return v_result
    
  

print(text_match(text))