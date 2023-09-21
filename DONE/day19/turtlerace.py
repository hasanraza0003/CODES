from turtle import Turtle,Screen
import random

is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet =screen.textinput(title="Make your bet",prompt="which colour of the turtle win the race ? enter the colour : ")
colors=["red","yellow","orange","green","blue","purple"]
y_positions = [-70,-40,-10,20,50,80]
all_turtles=[]

for turtle_index in range(6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(-230,y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

print(all_turtles)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on=False
            winning_colour = turtle.pencolor()
            if winning_colour==user_bet:
                print (f"You won, {winning_colour}")
            else:
                print(f"You lose! the winner is {winning_colour}")
    
    
        rand_dist= random.randint(0,10)
        turtle.forward(rand_dist)

screen.exitonclick()