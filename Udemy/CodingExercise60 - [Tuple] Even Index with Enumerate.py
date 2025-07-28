#ANCHOR - Even Index with Enumerate
"""
Implement a function which takes as a parameter a tuple and return a new tuple but only have even index elements from original tuple.

Hint : Use enumerate() function

Example

my_tuple = ("a", "b", "c", "d", "e", "f", "g")
even_index_items(my_tuple)
Output

('a', 'c', 'e', 'g')

"""

my_tuple = ("a", "b", "c", "d", "e", "f", "g")

def even_index_items(p_tuple):
    result_list = []
    
    for index, value in enumerate(p_tuple):
      print(index, index % 2)
      if not index % 2:
        result_list.append(value)     #TODO - insert value of tuple in list
    result_tuple = tuple(result_list)     #TODO - insert list to tuple
    return result_tuple

my_tuple = ("a", "b", "c", "d", "e", "f", "g")
result = even_index_items(my_tuple)
print(result)