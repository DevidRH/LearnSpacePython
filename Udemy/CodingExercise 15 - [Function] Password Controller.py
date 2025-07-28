#ANCHOR - Password Controller
"""
Create a function which takes string password as a parameter and checks the length of password. 
If the length longer than 8 character it returns True otherwise returns False.

Example:

password_controller("custompassword")

output:

True

"""

def pass_controller(password_):
  if len(password_) <= 8:
    return "False"
  return "True"

input_password = input("Input Password = ")

print(pass_controller(input_password))

 