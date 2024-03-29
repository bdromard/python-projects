# Importation of classes and libraries.
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time





# Screen initialization.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sneaky Snek")
screen.tracer(0)
# Objects creation : Snake and Food
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Event listening initialization, with arrow keys used as inputs.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game initialization
game_is_on = True
while game_is_on:
    # Modify screen with every snake movement
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with Food and reset Food's position
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()