#ANCHOR - Remove Empty Items
"""
Implement a function which takes as a parameter dictionary and removes empty items from it and return new dictionary. 
If there is not any empty item in the dictionary it will return itself.

Example

custom_dict = {
    "name" : "Elshad",
    "age" : 28,
    "city" : None
}
remove_empty_items(custom_dict)
Output

{'name': 'Elshad', 'age': 28}

"""

custom_dict = {
    "name" : "Elshad",
    "age" : 28,
    "city" : None
}

"""
In Python, when you iterate over a dictionary and modify it at the same time (like removing keys), 
it can cause unexpected behavior or even raise a RuntimeError. 
The reason is that you're changing the size of the dictionary while looping over it — which is generally not safe.
The list() creates a copy of the dictionary's (key, value) pairs as a separate list. 
So instead of looping over the live view of the dictionary, you're looping over a static copy. 
That means you can safely modify custom_dict (e.g., remove keys) during the loop.
"""

for key_, value_ in list(custom_dict.items()):
  if value_ is None:
    custom_dict.pop(key_)
  

print(custom_dict)