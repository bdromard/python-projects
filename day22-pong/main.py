from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen initialization.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pung")
screen.tracer(0)

# Objects creation : two Paddles, one Ball.
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Event listening initialization, with arrow keys used as inputs.
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "z")
screen.onkey(l_paddle.go_down, "s")

# Game initialization
game_is_on = True
while game_is_on:
    # Modify screen with every snake movement
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with both paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if ball goes out of bounds on the right
    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()

    # Detect if ball goes out of bounds on the left
    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()

screen.exitonclick()