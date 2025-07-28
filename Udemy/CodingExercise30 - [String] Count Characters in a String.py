#ANCHOR - Count Characters in a String
"""
Implement a function count_letter that takes two parameters : a string and a letter, then returns the  number of times the letter  appears in a string

Example:

count_letter("Learning Python", "n")
Output

3
"""

def count_letter(p_sentence, p_letter):
  count_letter = 0
  for i in p_sentence:
    if i == p_letter:
      count_letter += 1
  
  return count_letter

input_sentence = input("Enter a sentence : ")
input_letter = input("Enter a letter to count : ")

print(count_letter(input_sentence, input_letter))