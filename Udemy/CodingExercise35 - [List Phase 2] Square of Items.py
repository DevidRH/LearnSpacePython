#ANCHOR - Square Of Items
"""
Implement a function that takes a list as a parameter and turn list items into their square.

Example

custom_list = [1,2,3,4,5]
square_list(custom_list)
Output

[1,4,9,16,25]

"""
custom_list = [1,2,3,4,5]

def square_list(p_list):
  for index in range(len(p_list)):
    list_ = p_list[index] * p_list[index]
    print(list_, end= " ")
    
square_list(custom_list)

