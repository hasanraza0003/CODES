from art import logo
print(logo)
import random
list=[]
for i in range(1,101):
    list.append(i)
def guess_num():
    print("Welcome to the Number Guessing Game!")
    num=random.choice(list)
    number=int(input("Guess the Number Between 1-100 \n"))
    if number>num:
        print("Too High")
    elif number<num:
        print("Too Low")
    elif number==num:
        print(f"The Number is correct , that is {num}")
user_choice=input("Which Level Do You Want To Play The Game  'hard' or 'easy'")
turn=0
if user_choice=="hard":
        while turn!=10:
         guess_num()
         turn+=1
         if turn==10:
          print("Game Over")
elif user_choice=="easy":
      while turn!=5:
        guess_num()
        turn+=1
        if turn==5:
            print("\nGame Over")

        




