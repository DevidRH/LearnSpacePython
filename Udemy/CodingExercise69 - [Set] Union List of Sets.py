#ANCHOR - Union List of Sets
"""
Implement a function which takes list of sets as a parameter and returns one set which includes all elements from the given list of sets.

list_of_sets = [
    {10,20,30,40,50},
    {"apple", "orange","limon","pear"},
    {"London", "Berlin", "Paris"},
    {"Python", "Java", "Swift"},
    {10, "ten", "20", 20}
]
Input

convert_ls(list_of_sets)
Output

{'limon', 'pear', 'Java', 'orange', 10, 'Swift', 'apple', 20, 'Python', 'Paris', 30, '20', 'London', 'ten', 40, 50, 'Berlin'}

"""

list_of_sets = [
    {10,20,30,40,50},
    {"apple", "orange","limon","pear"},
    {"London", "Berlin", "Paris"},
    {"Python", "Java", "Swift"},
    {10, "ten", "20", 20}
]

def convert_list_to_set(p_list):
  new_set1 = set()
  new_set2 = set()
  new_list = list()
  
  for element1 in p_list:
    new_set1.add(element1)
    for element2 in p_list[element1]:
      new_set2.add(element2)
  
  return f"set 1 : {new_set1}, set 2 : {new_set2}"

print(convert_list_to_set(list_of_sets))
