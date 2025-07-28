#ANCHOR - Remove Duplicates
"""
How can we remove duplicates from given List using Set?

Example

my_list = ["apple", "apple", "orange", "grape", "grape", "orange", "apple"]

Output

['grape', 'apple', 'orange']

"""

my_list = ["apple", "apple", "orange", "grape", "grape", "orange", "apple"]

def remove_duplicate(p_list):
  my_set = set()
  
  for element_ in p_list:
    my_set.add(element_)
    
  new_list = list(my_set)
  
  return new_list

"""
OR
my_set = set(my_list)
print(my_set)
my_list = list(my_set)
print(my_list)
"""

print(remove_duplicate(my_list))