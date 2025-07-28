#ANCHOR - Adding even numbers in ANY range

def sum_range_number(p_start, p_end):
  total = 0
  for i in range(p_start, p_end+1):
    if i % 2 == 0:
      total += i
  return total
  
print(sum_range_number(1, 100))