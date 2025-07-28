#ANCHOR - Adding Odd Numbers

def sum_odd_numbers(p_start, p_end, p_multiple):
  init = 0
  for i in range(p_start, p_end, p_multiple):
    init += i
  return i, init
  
print(f"total {sum_odd_numbers(1, 101, 2)}")
