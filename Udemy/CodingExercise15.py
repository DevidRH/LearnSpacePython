#ANCHOR - Password controller

def pass_controller(password_):
  if len(password_) <= 8:
    return "False"
  return "True"

input_password = input("Input Password = ")

print(pass_controller(input_password))

 