#ANCHOR - Format a String
"""
Use find and string slicing to extract the portion of the string after the colon character and then 
use the float function to convert the extracted string into a floating point number.

custom_string = 'X-MAPDS-Confidence:0.8475'

Output

0.8475

"""

custom_string = 'X-MAPDS-Confidence:0.8475'

index_string = custom_string.find(":")

extracted_string_to_float = float(custom_string[index_string+1:])

print(index_string)
print(extracted_string_to_float)