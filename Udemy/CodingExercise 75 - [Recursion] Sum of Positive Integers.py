#ANCHOR - Sum of Positive Integers

"""
Implement a function to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).

Example

sum_positive(10)

Output

30

"""

def sum_positive(n):
  if not isinstance(n, int):
    return -1
  elif n < 1:
    return 0
  else:
    v_result = n + sum_positive(n-2)
    return v_result
  
print(sum_positive(5))