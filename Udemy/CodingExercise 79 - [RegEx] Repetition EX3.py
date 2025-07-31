#ANCHOR - Repetition EX3
"""
Write a Python function that matches given words in the text and count them.

Words: Love, love, Lovers, lovers

Text: Lovers in love

Lovers in love

Love, love, love, love, love

Love, love, love, love, love

Love, love, love, love, love

Love, love, love, love, love

Lovers loving love just like these lovers are loving love in love

Lovers loving love just like these lovers are loving love in love

Input

text_match(text)
Output

34

"""

import re

text = '''Lovers in love
Lovers in love
Love, love, love, love, love
Love, love, love, love, love
Love, love, love, love, love
Love, love, love, love, love
Lovers loving love just like these lovers are loving love in love
Lovers loving love just like these lovers are loving love in love'''

def text_match(p_text):
  regex_pattern = re.compile(r"(L|l)ove(rs)?")      #NOTE - () for grouping to be one char, | is or, ? for make rs is optional
  
  text_list = p_text.split()      #TODO - to split per word in insert into list
  
  v_count = 0
  for f_word in text_list:
    x = regex_pattern.search(f_word)
    if x != None:
      v_count += 1
      
  return v_count


print(text_match(text))