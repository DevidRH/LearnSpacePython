#ANCHOR - Multiply Dictionary Items
"""
Implement a function which takes dictionary as a parameter and returns multiplication of values of this dictionary.

Example

my_dict = {"One" : 1, "Two" : 2, "Three" : 3, "Four" : 4}
multiply_values(my_dict)
Output

24

"""

my_dict = {"One" : 1, "Two" : 2, "Three" : 3, "Four" : 4}

def multiply_values(p_dictionary):
  multiplication_result = 1
  for key_ in p_dictionary:
    multiplication_result *= p_dictionary[key_]
  return multiplication_result
  
print(multiply_values(my_dict))