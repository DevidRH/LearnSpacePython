#ANCHOR - Custom Deep Copy for List Values
"""
Implement custom deep copy method for a dictionary where the values are lists.

Example

original_dict = {
    "names" : ["Elshad", "John", "Edy"],
    "numbers" : [1,2,3,4,5]
}
 
copied_dict = deep_copy(original_dict)
copied_dict["names"].append("Jack")
copied_dict["numbers"].append(6)
 
print(original_dict)
print(copied_dict)
Output

{
    'names': ['Elshad', 'John', 'Edy'], 
    'numbers': [1, 2, 3, 4, 5]
}
 
{
    'names': ['Elshad', 'John', 'Edy', 'Jack'], 
    'numbers': [1, 2, 3, 4, 5, 6]
}
"""
import copy

original_dict = {
    "names" : ["Elshad", "John", "Edy"],
    "numbers" : [1,2,3,4,5]
}

def deep_copy(p_dict):
  not_original_dict = copy.deepcopy(p_dict)
  return not_original_dict

copied_dict = deep_copy(original_dict)
copied_dict["names"].append("Jack")
copied_dict["numbers"].append(6)
 
print(original_dict)
print(copied_dict)
