#ANCHOR - Painting the Wall
"""
We need to paint a wall and we do not know how many cans of paint we need to buy. 
The instructions on the paint can says that 1 can of paint can cover 4 square meters of wall. 
So we need to define a function which takes as parameter  height and width of wall and  
calculates the area of the wall and based on the area we can calculate number of cans of paint that we need.

Area of wall = wall height  *  wall width

Number of cans of paint that is needed =  Area of wall ÷ coverage per can.

Example

Height = 2, Width = 5, Coverage = 4

Area of wall = 2  *  5  = 10

Number of cans of paint that is needed =  10 ÷ 4 = 2.5

But because you can't buy 2.5 of a can of paint, the result should be rounded up to 3 cans.

Hint: To round up number ceil function from math module can be used. Math.ceil()

"""
import math

def cans_needed(height_, width_, coverage_):
  area_of_wall = height_ * width_
  total_cans = math.ceil(area_of_wall / coverage_)      #NOTE - math.ceil is built-in function from module math that round up decimal number
  print(f"Number of cans we needed : {total_cans}")


height_ = int(input("Height of the wall : "))
width_ = int(input("Width of the wall : "))

cans_needed(height_, width_, 4)