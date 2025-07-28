#ANCHOR - Concatenate Two Lists in One List Item Wise
"""
Implement a function which takes two lists as parameter and return concatenation of these lists item wise.

Example

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
concatenate(list1, list2)
Output

['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

"""

def concatenate(p_list1, p_list2):
  item_list3 = []
  for i in p_list1:
    for j in p_list2:
      item_list3 = item_list3 + [i + j]
  print(item_list3)

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

concatenate(list1, list2)