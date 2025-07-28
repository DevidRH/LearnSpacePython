#ANCHOR - Count Characters in a Word
"""
Implement a function that takes a String as a parameter and returns a dictionary with characters as keys from the String 
and values are the occurrence of characters in the String. Basically we are counting the occurrence of characters in a given string 
and returning it as output in Dictionary.

Example

count_character("BABACDAS")
Output

{
 'B': 2, 
 'A': 3, 
 'C': 1, 
 'D': 1, 
 'S': 1
} 

"""


# input_value = input("Input Character : ")
sentences_ = "lalalalilili"
def count_characters(p_char):
  p_char = dict()
  for i in sentences_:
    if i not in p_char:
      p_char[i] = 1
    else:
      p_char[i] = p_char[i] + 1
  return p_char

print(count_characters(sentences_))



