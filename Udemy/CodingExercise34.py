#ANCHOR - Print Pattern
"""
Create a function which takes as parameter integer number (n) and based on this number it prints 
the following start pattern using nested loop and string formatting. 
So if n equals 5 the maximum number of stars (*) will be 5 in the pattern.

Example1

print_pattern(5)

Output1

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
Example2

print_pattern(6)

Output1

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

"""


def pattern_star(p_input):
  #TODO - Ascending looping
  for i in range(1, p_input+1):
    for j in range(i):
      print("*", end=" ")     #NOTE - end=" " keeps stars on the same line with spaces.
    print()   #NOTE - print() after the inner loop moves to the next line or new line.
    
  #TODO - Descending looping
  for i in range(p_input-1, 0, -1):
    for j in range(i):
      print("*", end= " ")    #NOTE - end=" " keeps stars on the same line with spaces.
    print()   #NOTE - print() after the inner loop moves to the next line.
  
    

input_number = int(input("Enter a number : "))

print(pattern_star(input_number))
    