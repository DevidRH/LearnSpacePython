#ANCHOR - Factorial
import math

try:
    insert_number = int(input("Enter a number: "))
    factorial_ = math.factorial(insert_number)      #NOTE - Factorial built-in function from module math
    
    print(f"The factorial of {insert_number} is: {factorial_}")
except:
  print('Please insert a number')
