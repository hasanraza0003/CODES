import turtle as t
import pandas as pd
screen = t.Screen()
screen.title("India States Game")
image = r"indiastate game\india.gif"
screen.addshape(image)
t.shape(image)
x = pd.read_csv(r"indiastate game\indiastate.csv")
state_names= x.state.tolist()
guessed_list=[]
while len(guessed_list) < 50:
    answer = screen.textinput(title=f" {len(guessed_list)} / 29  India State Guessing game?", prompt="Enter The State Name : ").title()
    if answer in state_names:
        guessed_list.append(answer)
        p=t.Turtle()
        p.hideturtle()
        p.penup()
        cor=x[x.state == answer]
        p.goto(int(cor.x),int(cor.y))
        p.write(answer)
    elif answer == "Exit":
        learning_list=[state for state in state_names if state not in guessed_list]
        list=pd.DataFrame(learning_list)
        list.to_csv("learning_list")
        break
screen.exitonclick()