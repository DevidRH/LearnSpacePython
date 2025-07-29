#ANCHOR - 'a' to the power 'b' - using Recursion
"""
Implement a function to calculate the value of 'a' to the power 'b' using Recursion for positive integer numbers.

Example

power(2,4)


Output
2*2*2*2
16

"""

def power(p_a, p_b):
  if not isinstance(p_a, int) or not isinstance(p_b, int) or p_b < 0:
    return "not applicable"
  elif p_b == 0:
    return 1
  elif p_a == 0:
    return 0
  elif p_b == 1:
    return p_a
  else:
    v_result = p_a * power(p_a, p_b - 1)
    return v_result
  
print(power(5, 2))