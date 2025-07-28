#ANCHOR - Numbers divisible by 5 until 130
#NOTE - Implement a function which takes a given ordered list as a parameter and displays numbers divisible by 5 and if a number is greater than 130 display STOP in the console.

list_numbers = [12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200] 

def numbers_divisible_by_five(p_list_numbers):
  number_div = 0
  for number_ in p_list_numbers:
    number_div = number_ % 5    #NOTE - for get data div 0 when number_ divide 5, like 15/5 is 3.0
    if number_div != 0:
      continue    #NOTE - built-in funcion continue for skip if condition true and bypass to print(number_)
    elif number_ > 130:
      break   #NOTE - built-in function breaks for stop looping when condition is true
    print(number_)
  
numbers_divisible_by_five(list_numbers)