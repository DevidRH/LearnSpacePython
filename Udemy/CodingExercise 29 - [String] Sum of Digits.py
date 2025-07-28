#ANCHOR - Sum of Digits

"""
Write a program which asks for any given integer number from the console and prints out the sum of digits of given number.

Input

Enter an integer number: 134

Output

8

"""

input_number = input("Enter an integer number : ")

index_ = 0
total_ = 0
for i in input_number:
  
  slice_of_input = input_number[index_]
  
  slice_of_input = int(slice_of_input)
  total_ += slice_of_input
  
  print(index_, slice_of_input)
  
  index_ += 1

print(total_)