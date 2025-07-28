#ANCHOR - Format List

"""
Print a given list in the format that is shown below using join method.

custom_list = [1, 2, 3, 4, 5]

Output

1 | 2 | 3 | 4 | 5

"""

custom_list = [1, 2, 3, 4, 5]
output_list = []

for item in custom_list:
  output_list.append(str(item))
  # print(output_list)

custom_string = "|".join(output_list)
print(custom_string) 