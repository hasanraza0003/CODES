names= ["Alex", "Beth" , "Caroline" , "Dave" ,"Elanor" , "Freddie" ]
import random

student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)


passed_student = {pstudent:pscore  for (pstudent , pscore)  in student_scores.items() if pscore >=60}
print(passed_student)

# dict.items() used for convert dictionary data into list in the tuples form (key , values)


# problem 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
x=list(sentence.split())
result = {text: (len(text)) for text in x}
# Write your code below:
print(result)

# problem 2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
# Write your code 👇 below:
weather_f = {new:f*(9/5)+32 for (new,f) in weather_c.items()}
print(weather_f)



