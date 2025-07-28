#ANCHOR - Student Grades
"""
Implement a function which takes a dictionary as a parameter in which student scores are stored and converts their scores to grades and return it as new dictionary.

This is the scoring criteria:

Scores 85 - 100: Grade = "Outstanding"
Scores 65 - 84: Grade = "Good"
Scores 50 - 64: Grade = "Acceptable"
Scores 50 lower: Grade = "Fail"
Example

student_scores = {
  "John": 90,
  "Edy": 68,
  "Marry": 88, 
  "Ewan": 79,
  "Park": 62,
}
convert_grade(student_scores)
Output

{
 'John': 'Outstanding', 
 'Edy': 'Good', 
 'Marry': 'Outstanding', 
 'Ewan': 'Good', 
 'Park': 'Acceptable'
} 

"""

student_scores = {
  "John": 90,
  "Edy": 68,
  "Marry": 88, 
  "Ewan": 79,
  "Park": 62,
}

def convert_grade(p_dictionary):
  student_grade = dict()

  for key_ in p_dictionary:
    if p_dictionary[key_] <= 100 and p_dictionary[key_] >= 85:
      student_grade[key_] = "Outstanding"
    elif p_dictionary[key_] < 85 and p_dictionary[key_] >= 65:
      student_grade[key_] = "Good"
    elif p_dictionary[key_] < 65 and p_dictionary[key_] >= 50:
      student_grade[key_] = "Acceptable"
    elif p_dictionary[key_] < 50:
      student_grade[key_] = "Fail"
      
  return student_grade

print(convert_grade(student_scores))