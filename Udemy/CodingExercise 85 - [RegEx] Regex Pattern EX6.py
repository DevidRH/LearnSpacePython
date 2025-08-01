#ANCHOR - Regex Pattern EX6
"""
Write a Python function to find sequences of capital letters joined with a underscore. 
If match is found it returns Matched otherwise Not matched.

Example

text_match("BB_CCAA")
text_match("aabb_DDDEFF")
text_match("ADRGT_BCDEe")
Output

Matched
Not matched
Not matched

"""

import re

def text_match(p_text):
  regex_pattern = re.compile(r'^[A-Z]+_[A-Z]+$')      #NOTE - ^start, + index 1 or more occurence, $end all of capital
  x = regex_pattern.findall(p_text)
  print(x)
  if x:
    return "Matched"
  else:
    return "Not Matched"
  
  
  

print(text_match("BBAA_DDDEFF"))