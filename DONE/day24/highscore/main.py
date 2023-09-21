from turtle import Turtle,Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen= Screen()
screen.setup(width=1000,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

food = Food()
snake = Snake()
scoreboard = Scoreboard()

snake.play_game()

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detecting collision with food
    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    #detect collision with wall
    if snake.head.xcor() > 490 or snake.head.xcor() < -490 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        
    #detect collision with tail :
    for segment in snake.segments[1:]:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment) < 10:  
            scoreboard.game_over()
            snake.reset()

screen.exitonclick() 



