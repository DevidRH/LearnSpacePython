#ANCHOR - Find Most Frequent Item
"""
Implement a function which takes a tuple as a parameter and returns another tuple with two elements. 
First element is the most frequent item and the second element of number of repetition.

Hint: Use count() method

Example

my_tuple = ("a","b","c","d","e","a","c","e","b","e","c","a","f","e","r")
most_frequent(my_tuple)
Output

('e', 4)

"""
my_tuple = ("a","b","c","d","e","a","c","e","b","e","c","a","f","e","r")
def most_frequent(p_tuple):
  max_count = 0
  item_ = p_tuple[0]
  
  for value_ in p_tuple:
    current_item_count = p_tuple.count(value_)
    if current_item_count > max_count:
      max_count = current_item_count
      item_ = value_
    print(value_, current_item_count)
  
  return (item_, max_count)

print(most_frequent(my_tuple))