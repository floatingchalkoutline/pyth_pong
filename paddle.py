from turtle import Turtle

UP = 90
DOWN = 270
TOP_EDGE = 320
BOTTOM_EDGE = -320
turn = True


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=4, stretch_len=1)

    def check_paddle_edge(self):
        if self.ycor() + 80 > 400 or self.ycor() - 80 < -400:
            if self.ycor() > 0:
                self.sety(TOP_EDGE)
            else:
                self.sety(BOTTOM_EDGE)
            return False
        else:
            return True

    def move_up(self):
        if self.check_paddle_edge():
            self.setheading(90)
            self.forward(40)
            self.setheading(0)

    def move_down(self):
        if self.check_paddle_edge():
            self.setheading(270)
            self.forward(40)
            self.setheading(0)

    def auto_move(self):
        global turn
        if self.ycor() > 315:
            turn = True
        elif self.ycor() < -315:
            turn = False
        if turn:
            self.move_down()
        elif not turn:
            self.move_up()
