from turtle import Turtle, Screen
from paddle import Paddle
from net import Net
from scoreboard import Scoreboard
from ball import Ball
import time


# initiate the Screen with settings
screen = Screen()
screen.title("PONG")
screen.setup(width=1600, height=800)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

# initiate the net, scoreboard, paddles, and ball
net = Net()
scoreboard = Scoreboard()
player_paddle = Paddle()
cpu_paddle = Paddle()
ball = Ball()

# set the paddles to their starting positions
player_paddle.goto(-780, 0)
cpu_paddle.goto(780, 0)
# place the ball in the center
ball.start()

game_on = True
while game_on:
    # decide which keys control the player's paddle
    screen.onkey(player_paddle.move_up, "Up")
    screen.onkey(player_paddle.move_down, "Down")
    # move the ball
    ball.movement()
    # move the cpu_paddle automatically
    cpu_paddle.auto_move()
    # detect collision between player paddle and ball
    ball_player_x = ball.xcor() - player_paddle.xcor()
    ball_player_y = ball.ycor() - player_paddle.ycor()
    ball_cpu_x = ball.xcor() - cpu_paddle.xcor()
    ball_cpu_y = ball.ycor() - cpu_paddle.ycor()
    if (-20 < ball_player_x < 20) and (-80 < ball_player_y < 80):
        if ball.heading() == 135:
            ball.setheading(45)
        elif ball.heading() == 225:
            ball.setheading(315)
    elif (-20 < ball_cpu_x < 20) and (-80 < ball_cpu_y < 80):
        if ball.heading() == 45:
            ball.setheading(135)
        elif ball.heading() == 315:
            ball.setheading(225)
    # tally the scoreboard
    if ball.xcor() <= -800:
        scoreboard.point_cpu()
    elif ball.xcor() >= 800:
        scoreboard.point_player()
    if scoreboard.xcor() == 0 and scoreboard.ycor() == 0:
        game_on = False
    time.sleep(0.05)
    screen.update()

screen.exitonclick()
