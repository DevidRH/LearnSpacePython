#ANCHOR - Factorial
"""
Write a program that calculates the factorial (!) of any given number by a user.

3! = 3*2*1 = 6

4! = 4*3*2*1 = 24

Example Input

Enter a number: 4
Example Output

The factorial of 4 is: 24


Hint : Use math module to calculate factorial
"""


import math

try:
    insert_number = int(input("Enter a number: "))
    factorial_ = math.factorial(insert_number)      #NOTE - Factorial built-in function from module math
    
    print(f"The factorial of {insert_number} is: {factorial_}")
except:
  print('Please insert a number')
