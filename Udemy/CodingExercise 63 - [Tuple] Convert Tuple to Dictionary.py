#ANCHOR - Convert Tuple to Dictionary
"""
Implement a function which takes a list of tuples as a parameter and convert it to a dictionary and return the dictionary.

Example

tuple_list = [("one", 1), ("two", 2), ("three", 3), ("four", 4)]
convert_to_dict(tuple_list)
Output

{'one': 1, 'two': 2, 'three': 3, 'four': 4}

"""

tuple_list = [("one", 1), ("two", 2), ("three", 3), ("four", 4)]

def convert_to_dict(p_tuple):
  dict_converted = dict()
  
  for item_ in p_tuple:
    # dict_converted[item_[0]] = item_[1]   #NOTE - you can use this or
    key_, value_ = item_      #TODO - unpack tuple
    dict_converted.setdefault(key_, value_)
    
  return dict_converted
    

print(convert_to_dict(tuple_list))
    
  