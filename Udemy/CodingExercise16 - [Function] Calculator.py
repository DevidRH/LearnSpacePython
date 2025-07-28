#ANCHOR - Calculator
"""
Implement code block which asks two numbers and operation (+,-,*,/) that we want to perform on these numbers and returns the result.

For example

What is the first number? 2
What is the second number? 4
Pick operation from this list (+,-,*,/) *
Output

2 * 4 = 8
"""

#NOTE - n1 is number 1, n2 is number 2

def add_(n1, n2):
  calculated_ = n1 + n2
  return calculated_

def substract_(n1, n2):
  calculated_ = n1 - n2
  return calculated_

def multiple_(n1, n2):
  calculated_ = n1 * n2
  return calculated_

def divided_(n1, n2):
  calculated_ = n1 / n2
  return round(calculated_, 2)

f_number = int(input("What is the first number ? "))
s_number = int(input("What is the second number ? "))
operator_ = input("Pick operatioin from this list (+, -, *, /) ? ")

if operator_ == "+":
  print(add_(f_number, s_number))
elif operator_ == "-":
  print(substract_(f_number, s_number))
elif operator_ == "*":
  print(multiple_(f_number, s_number))
elif operator_ == "/":
  print(divided_(f_number, s_number))
else:
  print("Just insert what on the list above !!!")