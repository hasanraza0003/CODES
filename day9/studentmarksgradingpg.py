student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for score in student_scores:
    if student_scores[score]>90 and student_scores[score]<100  :
        student_grades[score]="outstanding"
    elif student_scores[score]>80 and student_scores[score]<90 :
        student_grades[score]="exceeds expectation"
    elif student_scores[score]>70 and student_scores[score]<80 :
        student_grades[score]="acceptable"
    else:
        student_grades[score]="fail"
    
# 🚨 Don't change the code below 👇
print(student_grades)




