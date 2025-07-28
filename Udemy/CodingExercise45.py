#ANCHOR - List Addition with Function
"""
Implement a function which takes two parameters - a list and a value and returns new list with value inserted in it without modifying the original list.

Example

list1 = [1,2,3,4,5]
list2 = custom_insert(list1, 6)
print(list1)
print(list2)
Output

[1,2,3,4,5]
[1,2,3,4,5,6]

"""

def custom_insert(p_list, p_insert):
  new_list = p_list.copy()      #TODO - Create a shallow copy to avoid modifying the original
  new_list.append(p_insert)     #TODO - Add the new value
  return new_list

list1 = [1,2,3,4,5]
list2 = custom_insert(list1, 6)
print(list1)
print(list2)

# or

def custom_insert1(p_list1, value):
  copy_list = p_list1[:]
  copy_list.append(value)
  return copy_list

list3 = [1,2,3,4,5]
list4 = custom_insert1(list3, 6)
print(list3)
print(list4)