#ANCHOR - Maximum and Minimum of Input Numbers
"""
Write another program that prompts for a list of numbers as we did in previous exercises and at the end prints out both the maximum and minimum of the inputted numbers.

For Example

Enter a number: 1
Enter a number: 3
Enter a number: 2
Enter a number: 4
Enter a number: done
Output

Maximum number: 4.0, Minimum number: 1.0
"""

def check_the_input(p_input):
  try:
    v_input = float(p_input)
    return v_input
  except (ValueError, TypeError):
    print('Please insert a number')
    return False
  
list_input = []

while True:
  input_ = input("Enter a number : ")
  
  if input_ == "done":
    print(f"Maximum number is : {max(list_input)}")
    print(f"Minimum number is : {min(list_input)}")
    break
  
  input_ = check_the_input(input_)
  
  if input_ is not False:
      list_input.append(input_)  # use append, not insert
      


