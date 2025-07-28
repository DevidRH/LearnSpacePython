#ANCHOR - Find Integer Numbers
"""
Implement a program which finds integer numbers from given List.

Input

custom_list = [11, 30.1, 90.2, 30, 45.1, 54, '54']

Output

11
30
54

"""

custom_list = [11, 30.1, 90.2, 30, 45.1, 54, '54']

for list_int in custom_list:
  if type(list_int) == int:
    print(list_int)
    

#NOTE - or using built-in function

for item in custom_list:
  if isinstance(item, int):
    print(f"with built-in function {item}")