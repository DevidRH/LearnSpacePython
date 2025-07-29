#ANCHOR - Sum of List using Recursion
"""
Implement a function which takes a list as a parameter and calculates the sum of a list of numbers.

sum_list([1, 2, 3, 4, 5])
Output

15

"""

my_list = [1, 2, 3, 4, 5]

def sum_list(p_list):
  #NOTE - The assert statement in Python is used to test assumptions in your code. 
  #NOTE - If the condition is True, nothing happens. 
  #NOTE - But if it’s False, Python raises an AssertionError, which stops the program (unless you handle
  # assert p_list >= 0 and int(p_list) == p_list, "list cannot negatif or decimal"
  
  if not isinstance(p_list, list):
    return -1
  elif len(p_list) == 1:
    return p_list[0]
  else:
    total = p_list[0] + sum_list(p_list[1:])
    return total
  
print(sum_list(my_list))


"""
total = 1 + sum_list([2, 3, 4, 5])
total = 1 + 2 + sum_list([3, 4, 5])
total = 1 + 2 + 3 + sum_list([4, 5])
total = 1 + 2 + 3 + 4 + sum_list([5])
total = 1 + 2 + 3 + 4 + 5 → 15

Visual Flow
sum_list([1, 2, 3, 4, 5])
= 1 + sum_list([2, 3, 4, 5])
= 1 + 2 + sum_list([3, 4, 5])
= 1 + 2 + 3 + sum_list([4, 5])
= 1 + 2 + 3 + 4 + sum_list([5])
= 1 + 2 + 3 + 4 + 5
= 15

Now we go back up the recursion stack:
Fourth call: sum_list([4, 5]) → 4 + 5 = 9
Third call: sum_list([3, 4, 5]) → 3 + 9 = 12
Second call: sum_list([2, 3, 4, 5]) → 2 + 12 = 14
First call: sum_list([1, 2, 3, 4, 5]) → 1 + 14 = 15

🔄 What Is the Call Stack?
When you call a function in Python, Python adds that call to the call stack — a structure that works like a stack of dishes:

The last thing added is the first thing removed (LIFO: Last In, First Out)

🧠 How This Affects Recursion
Each time sum_list() calls itself:

Python pauses the current function.

Stores the current state (like p_list[0]) on the call stack.

Starts working on the new, smaller problem (p_list[1:]).

But Python can’t complete the first call until the inner ones finish. So, it "dives down" the recursive calls first...

plaintext
Copy
Edit
sum_list([1, 2, 3, 4, 5])
 ↳ sum_list([2, 3, 4, 5])
    ↳ sum_list([3, 4, 5])
       ↳ sum_list([4, 5])
          ↳ sum_list([5])   ← Base case (returns 5)
Then Python starts resolving the functions from the bottom up (reverse of the call order):

plaintext
Copy
Edit
↳ sum_list([5]) returns 5
↳ sum_list([4, 5]) = 4 + 5 = 9
↳ sum_list([3, 4, 5]) = 3 + 9 = 12
↳ sum_list([2, 3, 4, 5]) = 2 + 12 = 14
↳ sum_list([1, 2, 3, 4, 5]) = 1 + 14 = 15
📦 Visual Analogy: Stack of Boxes
Imagine this:

You open 5 nested boxes to get the final number.

You can't close Box 4 until you know what's inside Box 5.

So, you close Box 5 first, then 4, 3, and so on.

That's what the "reversing" means — not that Python flips anything, 
but that it resolves from the last function call back up to the first.
"""