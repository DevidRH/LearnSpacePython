#ANCHOR - Sum of Digits of 2 Digit Number
"""
Create a function that takes two digit number from console and returns sum of digits. e.g. if the input was 45, then the output should be 4 + 5 = 9

Example Input

sum_of_two_digits()
Enter two digit number: 45 
Output

4 + 5  = 9

9
"""



def sum_sum_of_two_digits(p_input):
  
  if len(p_input) == 2:
    
    first_index = p_input[0]
    first_index = int(first_index)
    second_index = p_input[1]
    second_index = int(second_index)
    
    sum_index = first_index + second_index
    
    return f"{first_index} + {second_index} = {sum_index}"
  else:
    return "Please insert 2 digit number"
  
input_number = input("Enter two digit number : ")

print(sum_sum_of_two_digits(input_number))
