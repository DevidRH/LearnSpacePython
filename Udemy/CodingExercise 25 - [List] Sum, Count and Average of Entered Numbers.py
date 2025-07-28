#ANCHOR - Sum, Count and Average of Entered Numbers

"""
Write a program which repeatedly reads numbers until the user enters "done". Once “done” is entered, print out the total, count, and average of the numbers.

If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

Step 1 - Create a function which checks for numbers using try and except block.

Step 2 - Inside while loop ask for input

Step 3 - Calculate count, sum and average

Enter a number: 2
Enter a number: 4
Enter a number: six
Error, please enter numeric input
Enter a number: 6
Enter a number: done
12.0 3 4.0

"""


def check_number(p_input):
  try:
    input_ = float(p_input)
    return input_
  except (ValueError, TypeError):     #NOTE - ValueError : happens when you give a value type, but its invalid (e.g int("abc")), TypeError : happens when you perform an operation on the wrong type (e.g., 'abc', + 5)
    print('Error, please insert numeric input!!')
    return False      #NOTE - because we are use this function inside the if statement, so it has return false
    
    
count_ = 0
sum_ = 0
average_ = 0



while True:     #TODO - this will infinity looping because default boolean is true
  v_input = input("Enter a number : ")
  if v_input == "done":
    print(f"Count is = {count_}")
    print(f"Sum is : {sum_}")
    print(f"Average is : {average_}")
    break
  else:
    # print(check_number(v_input))
    convert_input = check_number(v_input)
    count_ += 1
    sum_ += convert_input
    average_ = sum_ / count_
  
  
