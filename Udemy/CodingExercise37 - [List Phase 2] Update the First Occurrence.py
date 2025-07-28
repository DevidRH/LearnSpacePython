#ANCHOR - Update the First Occurrence (kemunculan pertama)

"""
Find the value of 50 in a given list, and if it is present, replace  the first occurrence of a value with 5.

For example

list1 = [10, 10, 5, 15, 50, 50, 20]
Output

[10, 10, 5, 15, 5, 50, 20]
"""

list1 = [10, 10, 5, 15, 50, 50, 20]
index_list = list1.index(50)
list1[index_list] = 5

print(list1)

