#ANCHOR - Comparing Tuples
"""
Implement a function which takes a string (sentence) as a parameter and 
returns a tuple in which the words from the given sentenced are ordered based on their length.

Example

order_words("Python is my favorite programming language")

Output

('is', 'my', 'Python', 'favorite', 'language', 'programming')
"""

def order_words(p_text):
  words_ = p_text.split()
  nested_list = list()
  for word_ in words_:
    nested_list.append((len(word_), word_))
    
  print(f"Nested List : {nested_list}")
  nested_list.sort()
  print(f"Nested List Sorted : {nested_list}")
  result_ = list()
  for length_, word_ in nested_list:
    result_.append(word_)
  return tuple(result_)

print(order_words("Python is my favorite programming language"))
