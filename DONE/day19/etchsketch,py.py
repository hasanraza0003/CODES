from turtle import Turtle,Screen

t=Turtle()
screen=Screen()

def move_fwd():
    t.forward(10)
def move_bwd():
    t.backward(10)
def clock():
    t.rt(10)
def anti_clock():
    t.lt(10)
def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkeypress(fun=move_fwd,key="w")
screen.onkeypress(fun=move_bwd,key="s")
screen.onkeypress(fun=clock,key="d")
screen.onkeypress(fun=anti_clock,key="a")
screen.onkey(fun=clear_screen,key="c")

screen.exitonclick()