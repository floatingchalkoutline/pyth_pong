from turtle import Turtle
import random

HEADINGS = [45, 135, 225, 315]
BALL_START_Y = [-380, -360, -340, -320, -300, -280, -260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20,
          0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.start()

    def start(self):
        self.goto(0, random.choice(BALL_START_Y))
        self.setheading(random.choice(HEADINGS))

    def movement(self):
        if self.xcor() <= -800:
            self.start()
        elif self.xcor() >= 800:
            self.start()

        if self.ycor() >= 400 and self.heading() == HEADINGS[0]:
            self.down_right()
        elif self.ycor() >= 400 and self.heading() == HEADINGS[1]:
            self.down_left()
        elif self.ycor() <= -400 and self.heading() == HEADINGS[3]:
            self.up_right()
        elif self.ycor() <= -400 and self.heading() == HEADINGS[2]:
            self.up_left()
        else:
            self.forward(40)

    def up_right(self):
        self.setheading(HEADINGS[0])

    def up_left(self):
        self.setheading(HEADINGS[1])

    def down_left(self):
        self.setheading(HEADINGS[2])

    def down_right(self):
        self.setheading(HEADINGS[3])
