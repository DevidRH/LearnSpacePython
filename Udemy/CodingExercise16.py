#ANCHOR - Simple Calculation using function

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