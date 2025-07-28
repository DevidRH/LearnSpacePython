#ANCHOR - Area of Circle
"""
Write a program that calculates the area of circle based on user input of radius using equation provided below. The output must be rounded to 2 decimal places.


Example Input

Enter Radius: 4
Example Output

The area of circle is: 50.27
"""

import math

try:
    input_radius = float(input("Enter Radius : "))

    area_ = math.pi * (input_radius ** 2)        #NOTE - the formula is area = phi * r.kuadrat

    print(f"Phi is {math.pi}")
    print(f"Radius is {input_radius ** 2}")

    print(f"The area of circle is : {round(area_, 2)}")
except:
  print('Please insert a number')
  quit()