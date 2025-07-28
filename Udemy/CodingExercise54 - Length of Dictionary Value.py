#ANCHOR - Length of Dictionary Values
"""
Implement a function which takes a dictionary as a parameter and returns new dictionary.  
In new dictionary the keys remain same but values will be another nested dictionary. 
Nested dictionary's keys will be values from original dictionary and values will be length of values from original dictionary. 
(I know it is confusing, see example below you will understand it :) )

Example

names_dict = {
    1 : "Elshad",
    2 : "Renad",
    3 : "Johanna",
    4 : "Appmillers"
}
value_length(names_dict)
Output

{
    1: {'Elshad': 6}, 
    2: {'Renad': 5}, 
    3: {'Johanna': 7}, 
    4: {'Appmillers': 10}
}
"""

from pprint import pprint

names_dict = {
    1 : "Elshad",
    2 : "Renad",
    3 : "Johanna",
    4 : "Appmillers"
}


def value_length(p_dict):
    length_names_dict = dict()
    for key_, value_ in p_dict.items():
        length_names_dict[key_] = {}            #TODO - insert key with empty value and we can init empty dict using {} or dict()
        # print(length_names_dict)
        length_names_dict[key_][value_] = len(value_)           #TODO - insert nested dict
        # print(length_names_dict)
    pprint(length_names_dict)
    

# for i in names_dict:
#     length_names_dict[i] = {}          #TODO - insert key with empty value
#     print(length_names_dict)
#     length_names_dict[i][names_dict[i]] = {}           #TODO - insert nested dict
#     print(length_names_dict)
#     length_names_dict[i][names_dict[i]][len(names_dict[i])] = len(names_dict[i]) + 1            #TODO - insert nested dict
    
    
value_length(names_dict)

