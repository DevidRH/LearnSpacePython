#ANCHOR - Repetition EX1
"""
Write a Python function that matches a string that has an 'A' followed by zero or more 'B's.

Input

text_match("A")
text_match("ABC")
text_match("ABBC")
Output

Matched
Matched
Matched

"""

import re

def text_match(p_text):
  regex_pattern = re.compile(r'AB*')      #NOTE - compiles the regex pattern 'AB*' into a reusable object. And *(asterix) Match the preceding character or group zero or more times
  x = regex_pattern.search(p_text)
  
  if x == None:
    return "Not Matched"
  else:
    return "Matched"

print(text_match("a".upper()))
print(text_match("aabb".upper()))
print(text_match("abc".upper()))
