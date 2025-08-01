#ANCHOR - Character Class EX3
"""
Implement regular expression pattern inside a function to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

check_char("ABCDEFabef1250")
check_char("*&%@#{")
Output

['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'e', 'f', '1', '2', '5', '0']
[]

"""
import re

def check_char(p_text):
  regex_pattern = re.compile(r'[a-zA-Z]|[0-9]')     #NOTE - or we can use -> re.compile(r'[a-zA-Z0-9]')
  x = regex_pattern.findall(p_text)
  return x

print(check_char("ABCDEFabef1250"))
print(check_char("*&%@#{"))