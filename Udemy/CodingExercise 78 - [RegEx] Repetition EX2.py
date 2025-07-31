#ANCHOR - Repetition EX2
"""
Write a Python function that matches a string that has an 'A' followed by TWO to THREE 'B'.

Input

text_match("A")
text_match("ABC")
text_match("ABBC")
Output

Not matched
Not matched
Matched

"""
import re

def text_match(p_text):
  regex_pattern = re.compile(r"AB{2,3}")      #NOTE - format to be abb
  x = regex_pattern.search(p_text)
  if x == None:
    return "Not Matched"
  else:
    return "Matched"
  
print(text_match("a".upper()))
print(text_match("ab".upper()))
print(text_match("abbc".upper()))