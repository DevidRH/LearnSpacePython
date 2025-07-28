#ANCHOR - Sum of Above Average Scores
"""
Implement a function which takes a List as a parameter and returns the sum of the scores which are above average.

Example

student_scores = [80, 60, 50, 65, 75, 55]
sum_score_above_average(student_scores) # 220


Hint : DO NOT use any built in function such as sum() and len() !

"""

student_scores = [80, 60, 50, 65, 75, 55]

def sum_score_above_avg(p_student_scores):
  total = 0
  count = 0
  for score in p_student_scores:
    total += score    #NOTE - total = total + score
    count += 1    #NOTE - count = count + 1. ini untuk row count total berapa kali looping
    
  average = total / count
  
  above_average_sum = 0
  for score in p_student_scores:
    if score > average:
      above_average_sum += score
      
  return above_average_sum

print(sum_score_above_avg(student_scores))
    