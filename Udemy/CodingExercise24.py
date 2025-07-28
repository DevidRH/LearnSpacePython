#ANCHOR - Factorial using loop

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
  
    