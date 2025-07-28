#ANCHOR - Adding Odd Numbers
"""
Implement a function that calculates the sum of all odd numbers from 1 to 100 by using range() function inside loop.

Example

1+3+5+...+97+99 = 2500

"""

def sum_odd_numbers(p_start, p_end, p_multiple):
  init = 0
  for i in range(p_start, p_end, p_multiple):
    init += i
  return i, init
  
print(f"total {sum_odd_numbers(1, 101, 2)}")
