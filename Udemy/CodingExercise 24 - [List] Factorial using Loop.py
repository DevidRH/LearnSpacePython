#ANCHOR - Factorial using Loop
"""
Implement a function that takes an integer number as a parameter and returns factorial of this number.

Factorial Equation (!)

5! = 5 x 4 x 3 x 2 x 1 = 120

4! = 4 x 3 x 2 x 1 = 24

If input is 0 then the return value will be: The factorial of 0 is 1

if input is a negative number then the return value will be: Factorial does not exist for negative numbers

Example

factorial(4) # The factorial of 4 is 24
factorial(-1)  # Factorial does not exist for negative numbers

"""

input_factorial = input("Input number : ")
int_ = int(input_factorial)

def factorial(p_num):
  fact = 1
  steps = []
  
  for i in range(p_num, 0, -1):     #NOTE - start from p_num down to 0, -1 from p_num
    fact *= i
    steps.append(str(i))      #NOTE - append every loops value
    
  expression_ = " x ".join(steps)
  return f"{p_num}! = {expression_} = {fact}"

# print(factorial(int_))

if int_ == 0:
  print("The factorial of 0 is 1")
elif int_ < 0:
  print("Factorial does not exist for negatice numbers")
else:
  print(factorial(int_))
  
    