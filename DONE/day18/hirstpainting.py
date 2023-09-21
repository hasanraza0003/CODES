# from turtle import Turtle, Screen
import random
import turtle as t

tim =t.Turtle()

# challenge 1
# drawing a square
# for _ in range(4):
#     t.forward(100)
#     t.lt(90)

# challenge 2
# drawing a road line 
# for _ in range(20):
#     tim.pendown()
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)


# challenge 3
# drawing a triangle 120,square 90 ,pentagon 72 .hexagon 60 .octagon 45 .nonagon 40 ,decagon 36
# tim.penup()
# tim.goto(-40,100)
# tim.pendown()

# method  1
# for _ in range(3):
#     tim.color("gold")
#     tim.forward(100)
#     tim.rt(120)
# for _ in range(4):
#     tim.color("dark green")
#     tim.forward(100)
#     tim.rt(90)
# for _ in range(5):
#     tim.color("medium purple")
#     tim.forward(100)
#     tim.rt(72)
# for _ in range(6):
#     tim.color("gray")
#     tim.forward(100)
#     tim.rt(60)
# for _ in range(8):
#     tim.color("red")
#     tim.forward(100)
#     tim.rt(45)
# for _ in range(9):
#     tim.color("lawn green")
#     tim.forward(100)
#     tim.rt(40)
# for _ in range(10):
#     tim.color("yellow")
#     tim.forward(100)
#     tim.rt(36)

# method 2
# clr = ["cornflowers" , "gold" , "darkorchid" , "black" , "gray" , "green" , "yellow"]
# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side in range(3,11):
#     tim.color(random.choice(clr))
#     draw_shape(shape_side)

# challenge 3
# clr = ["CornflowerBlue", "IndianRed" ,"gold" , "DeepSkyBlue","wheat","Slategrey", "Seagreen","Darkorchid" , "black" , "gray" , "green" , "yellow"]
# dir=[0,90,180,270]


# for _ in range (1000):
#     tim.pensize(10)
#     tim.speed("fastest")
#     tim.color(random_color())
#     tim.forward(20)
#     tim.setheading(random.choice(dir))

#challenge 5
# generating a random colour

t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colour=(r,g,b)
    return colour

#challenge 6
# drawing a spirograph
# tim.speed("fastest")

# def draw_spigraph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#         tim.color(random_color())

# draw_spigraph(5)

# challenge 7
# draw a hirst painting 10*10

# tim.penup()
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# num_of_dot = 100
# for _ in range(int(num_of_dot/10)):
#     for _ in range(int(num_of_dot/10)):
#         tim.penup()
#         tim.fd(40)
#         tim.pendown()
#         tim.dot(20,random_color())
#     tim.penup()
#     tim.setheading(90)
#     tim.fd(40)
#     tim.setheading(180)
#     tim.fd(int((num_of_dot /10)*40))
#     tim.setheading(0)









# screen =t.Screen()
# screen.exitonclick()