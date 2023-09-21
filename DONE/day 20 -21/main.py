from turtle import Turtle,Screen
from day24.snake import Snake
import time
from day24.food import Food
from day24.scoreboard import Scoreboard

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
        scoreboard.game_over()
        game_is_on=False
        
    #detect collision with tail :
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on=False
            scoreboard.game_over()



screen.exitonclick() 