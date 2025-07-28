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
def convert_ls(p_ls):
    final_set = set()
    for item in p_ls:
        final_set = final_set.union(item)
    return final_set

print(convert_ls(list_of_sets))

