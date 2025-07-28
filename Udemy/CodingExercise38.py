#ANCHOR - First and Last Characters
"""
Implement a function which takes the string type list as a parameter 
and returns the count of the number of strings 
where the string length is 2 or more and the first and the last characters are same.

Example

list1 = ['cbc', 'xyz', 'aba', '2332', 'abc']
count_words(list1)
Output

3
"""

list1 = ['cbc', 'xyz', 'aba', '2332', 'abc']


def count_list(p_index):
  count_list = 0
  for i in list1:
    if len(i) >= 2:
      if i[0] == i[-1]:
        count_list += 1
  return count_list
  

print(count_list(list1))




