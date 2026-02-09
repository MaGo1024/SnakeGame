import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
wall = 280

starting_position = [(0,0), (-20, 0), (-40, 0)]
segments = []

# create snake
snake = Snake()

# Create food
food = Food()

# Create scoreboard
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # move snake
    snake.move()


    # detect  collision with food
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend()
        score.increase_score()

    # detect collision with the wall
    if snake.head.xcor() > wall or snake.head.xcor() < -wall or snake.head.ycor() > wall or snake.head.ycor() < -wall:
        game_is_on = False
        score.game_over()

    # detect collision with tail
    for segment in snake.segments:
        # if head collides with any segment in the tail:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            # trigger game_over
            game_is_on = False
            score.game_over()

screen.exitonclick()