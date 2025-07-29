#ANCHOR - Find Numbers Divisible by 3 and 4 - Intersection (like inner join)
"""
Implement a function which takes a parameter N and returns Set of numbers which are divisible by 3 and 4 between 0 and N.

Example Input

divisible_by_3and4(100)

Output

{0, 96, 36, 72, 12, 48, 84, 24, 60}

"""


def divisible_by_3and4(p_number):
  set1 = set(range(0, p_number, 3))     #NOTE - start, end, step
  set2 = set(range(0, p_number, 4))     #NOTE - start, end, step
  intersection_ = set1.intersection(set2)
  return intersection_

print(divisible_by_3and4(100))