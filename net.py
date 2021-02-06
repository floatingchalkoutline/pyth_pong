from turtle import Turtle


class Net(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color("white")
        self.goto(0, -400)
        self.pensize(10)
        self.setheading(90)
        for _ in range(0, 800):
            if _ % 5 == 0:
                self.pendown()
                self.forward(10)
            else:
                self.penup()
                self.forward(10)