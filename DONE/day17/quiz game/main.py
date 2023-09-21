from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank=[]

for question in question_data:
    question_text=question["question"]
    question_answer=question["correct_answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)



x=QuizBrain(question_bank)
while x.still_has_question():
    x.next_question()

print("You have completed the quiz")
print(f"Your Final score was : {x.score}/{x.question_number}")