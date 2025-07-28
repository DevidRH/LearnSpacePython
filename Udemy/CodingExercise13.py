#ANCHOR - Painting the wall
import math

def cans_needed(height_, width_, coverage_):
  area_of_wall = height_ * width_
  total_cans = math.ceil(area_of_wall / coverage_)      #NOTE - math.ceil is built-in function from module math that round up decimal number
  print(f"Number of cans we needed : {total_cans}")


height_ = int(input("Height of the wall : "))
width_ = int(input("Width of the wall : "))

cans_needed(height_, width_, 4)