#ANCHOR - Create a List from Two Lists

"""
Given two lists create a third list by picking an odd-index element from the first list and even-index elements from the second.

list_one = [4, 12, 16, 21, 24, 28, 32]
list_two = [5, 10, 15, 20, 25, 30, 35]
Output

[12, 21, 28, 5, 15, 25, 35]

"""

list_one = [4, 12, 16, 21, 24, 28, 32]
list_two = [5, 10, 15, 20, 25, 30, 35]

list_three = []

def is_odd(p_number):
  return p_number % 2 != 0  #NOTE- True if remainder is not 0 (i.e., 1 or -1)

def is_even(p_number):
  return p_number % 2 == 0  #NOTE - True if remainder is not 0 (i.e., 2 or 4)

for i in range(len(list_one)):
  if i % 2 != 0:
    list_three.append(list_one[i])

for i in range(len(list_two)):
  if i % 2 == 0:
    list_three.append(list_two[i])
    
print(list_three)

print("----------------------------OR----------------------------")

list_three_v2 = list()
odd_element = list_one[1::2]
even_element = list_two[0::2]

list_three_v2 = odd_element + even_element

print(list_three_v2)