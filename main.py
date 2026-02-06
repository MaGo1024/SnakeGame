import time
from turtle import Turtle, Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_position = [(0,0), (-20, 0), (-40, 0)]
segments = []

# create snake
snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # move snake
    snake.move()





screen.exitonclick()