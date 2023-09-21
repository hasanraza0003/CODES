from turtle import Turtle , Screen
timmy = Turtle()
my_screen = Screen()
timmy.shape("turtle")
timmy.color("DarkRed")
timmy.forward(100)
timmy.backward(100)
# ***here we create a object called timmy and assign the Turtle() class into it

# how to access attributes in class ----
print(my_screen.canvheight)

# how to access methods in class ----
my_screen.exitonclick()

