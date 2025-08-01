#ANCHOR - Anchors
"""
Implement a Python function which takes text as a parameter and return the list of words which are three, four or five characters long.

Example

find_words("I like Python for Everyone course. It is the best one out there.")
Output

['like', 'for', 'the', 'best', 'one', 'out', 'there']
"""

import re

def find_words(p_text):
  regex_pattern = re.compile(r'\b\w{3,5}\b')
  x = regex_pattern.findall(p_text)
  
  return x

print(find_words("I like Python for Everyone course. It is the best one out there."))