#ANCHOR - Remove and Add
"""
Remove an element at index 4 in a given list and add it to the 2nd position and at the end of the list.

Output

[10, 44, 11, 57, 99, 33, 84, 11]

"""

custom_list = [10, 44, 57, 99, 11, 33, 84]

element_ = custom_list.pop(4)
custom_list.insert(2, element_)
custom_list.append(element_)

print(custom_list)
