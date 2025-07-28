#ANCHOR - Adding Even Numbers in ANY Range
"""
Implement a function which takes two parameters as start and end of range and returns sum of even numbers within given range.

Example

add_even_numbers(1,100)

Output

2550

"""

def sum_range_number(p_start, p_end):
  total = 0
  for i in range(p_start, p_end+1):
    if i % 2 == 0:
      total += i
  return total
  
print(sum_range_number(1, 100))