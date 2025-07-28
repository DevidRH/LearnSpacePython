#ANCHOR - Backward Traversal

"""
Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, 
printing each letter on a separate line, except backwards.

Input

Enter a string: Python

Output

n
o
h
t
y
P
"""


input_value = input("Enter a string : ")

for char in input_value[::-1]:      #NOTE - sequence[start:stop:step]
  print(char)

#TODO - slicing to reverse
"""
start: index where slicing begins

stop: index where slicing ends (exclusive)

step: how much to move each time (positive or negative)

Part	 |  Meaning
word	 |  The original string (e.g., "Python")
:	     |  No start or stop → include entire string
-1	   |  Step of -1 → move backward one character at a time

means: “start from the end, move backward through the whole string one character at a time.”
"""

print("-------------------------------------------------------------------------------")
for i in range(len(input_value) - 1, -1, -1):  # from last index to 0
  print(input_value[i])

"""
Part  |   Value   |   Meaning
start |   5       |   Start from the last index (because len("Python") - 1 = 5)
stop  |   -1      |   Stop before reaching -1, so it stops at index 0
step  |   -1      |   Step backwards (decrease i by 1 each time)

"""

print("-------------------------------------------------------------------------------")
index_ = -1
length_ = -1 * len(input_value)

while index_ >= length_:
  letter_ = input_value[index_]
  print(letter_)
  index_ -= 1