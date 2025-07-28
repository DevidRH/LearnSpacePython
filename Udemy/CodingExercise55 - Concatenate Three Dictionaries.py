#ANCHOR - Concatenate Three Dictionaries
"""
Implement a function which takes three dictionaries as parameters and 
concatenate them into one new dictionary without updating the current ones and 
returns new dictionary with all elements of these three dictionaries in it.

Hint : use update() method of dictionary.

Example

dict1={1: "one", 2: "two"}
dict2={3: "three", 4: "four"}
dict3={5: "five", 6: "six"}
 
concatenate(dict1,dict2,dict3)
Output

{
    1: 'one', 
    2: 'two', 
    3: 'three', 
    4: 'four', 
    5: 'five', 
    6: 'six'
}

"""

dict1={1: "one", 2: "two"}
dict2={3: "three", 4: "four"}
dict3={5: "five", 6: "six"}

def concenate_(p_dict1, p_dict2, p_dict3):
  concatenate_dict = dict()
  
  for i in p_dict1, p_dict2, p_dict3:
    concatenate_dict.update(i)
  
  return concatenate_dict


print(concenate_(dict1, dict2, dict3))