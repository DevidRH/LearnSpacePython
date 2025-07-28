#ANCHOR - Generate Dictionary
"""
Implement a function which takes integer number (n) as a parameter and returns dictionary with keys from 1 to n and values are square of the numbers from 1 to n.

Example

generate_dictionary(5)

Output

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

"""


def generate_dictionary(p_n):
  dictionary_ = {}      #NOTE - or we can init dictionary_ = dict() to create empty dictionary
  for i in range(p_n):
    dictionary_[i+1] = (i+1) ** 2
  return dictionary_
    

print(generate_dictionary(5))
  