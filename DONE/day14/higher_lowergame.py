import random
from game_data import data

def display(account):
    name=account['name']
    description=account['description']
    country=account['country']
    return f"{name},a {description} ,from{country}."

def check_ans(guess,f1,f2):
    if f1>f2:
        if guess=="a":
            return True
        else:
            return False
    elif f1<f2:
        if guess=="a":
            return False
        else:
            return True
        
score=0
cont=True
b=random.choice(data)

while cont:
    a=b
    b=random.choice(data)
    while a==b:
        b=random.choice(data)
    a1=display(a)
    b1=display(b)
    a2=print("Compare A :",a1)
    b2=print("Compare B : ",b1)
    a3=a["follower_count"]
    b3=b["follower_count"]
    guess=input("Which has more follower A or B")
    is_correct=check_ans(guess,a3,b3)

    if is_correct==True:
        score += 1
        print(f"You Are Right, Current Score is {score}")
    else:
        print(f"You Are Wrong, Your Score is {score}")
        cont=False