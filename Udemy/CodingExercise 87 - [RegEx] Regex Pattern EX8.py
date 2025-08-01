#ANCHOR - Regex Pattern EX8
# Write a Python function to extact the email addresses from the given string.

# text = """From test@appmillers.com Wen Jan  5 09:14:16 2022\nFrom info@appmillers.com Wen Jan  5 09:14:16 2022\nFrom elshad@appmillers.com Wen Jan  5 \nFrom redy@appmillers.com Wen Jan  5 \nFrom info@appmillers.com Wen Jan  5 """
# Example Input

# extract_email(text)
# Example Output

# ['test@appmillers.com', 'info@appmillers.com', 'elshad@appmillers.com', 'redy@appmillers.com', 'info@appmillers.com']

import re

text = \
"""
  From test@appmillers.com Wen Jan  5 09:14:16 2022\n
  From info@appmillers.com Wen Jan  5 09:14:16 2022\n
  From elshad@appmillers.com Wen Jan  5 \n
  From redy@appmillers.com Wen Jan  5 \n
  From info@appmillers.com Wen Jan  5 
"""

def extract_email(p_text):
  regex_pattern = re.compile(r'\w+@\w+\.com')
  x = regex_pattern.findall(p_text)
  
  return x
  
print(extract_email(text))


