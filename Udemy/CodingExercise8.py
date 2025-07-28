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