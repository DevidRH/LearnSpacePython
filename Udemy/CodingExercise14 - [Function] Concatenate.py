#ANCHOR - Concatenate
"""
Implement a function that takes two strings as parameters and returns their concatenation.

Example:

concatenate("face", "book")

output:

facebook
"""

def concat_(f_word, l_word):
  concat_word = f"{f_word}{l_word}"
  return concat_word

output_ = concat_("face", "book")
print(output_)