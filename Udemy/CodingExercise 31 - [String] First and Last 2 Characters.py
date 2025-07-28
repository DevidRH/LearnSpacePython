#ANCHOR - First and Last 2 Characters
"""
Implement a function which takes a string as a parameter and returns new string which is made of the first 2 and the last 2 chars from a given a string. 
If the length of given string is less than 2 then return empty string.

Example

first_last_characters('appmillers')

Output

aprs
"""

def first_last_character(p_word):
  print(len(p_word))
  if len(p_word) < 2:
    return "Empty"
  first_two_char = p_word[0:2]    #NOTE - start from index 0, end to index 2, no step
  last_two_char = p_word[-2:]     #NOTE - start from index -2, no end, no step
    
  return first_two_char + last_two_char
  

input_value = input("Enter string : ")

print(first_last_character(input_value))