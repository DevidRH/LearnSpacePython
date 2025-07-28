#ANCHOR - Adding Members from List
"""
Implement a function which takes as a parameter List and add elements to a Set and return a set.

Example

my_list = [3,4,5,1,1,3,4,9,8]
adding_set(my_list)
Output

{1, 3, 4, 5, 8, 9}



Note: The order of elements might be different.
"""

my_list = [3,4,5,1,1,3,4,9,8]

def adding_set(p_list):
  my_set = set(p_list)
  return my_set

"""
OR

def adding_set(p_list):
    result_set = set()
    for item in p_list:
        result_set.add(item)
    return result_set
    
"""


print(adding_set(my_list))