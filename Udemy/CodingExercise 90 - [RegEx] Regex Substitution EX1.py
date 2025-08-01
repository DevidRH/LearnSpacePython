#ANCHOR - Regex Substitution EX1
"""
Implement a Python function which takes as a parameter IP address, removes leading zeros from it and returns it.

Example

remove_zero("211.07.095.122")
Output

211.7.95.122

"""

import re

def remove_zero(p_ip):
  v_output = re.sub(r'\.[0]*', '.', p_ip)     #NOTE - [0] replace after '.'
  return v_output
print(remove_zero("211.07.095.122"))
