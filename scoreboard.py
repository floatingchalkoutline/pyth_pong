from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.cpu_score = 0
        self.player_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 320)
        self.ht()
        self.write_score()

    def point_player(self):
        self.clear()
        self.player_score += 1
        self.write_score()
        self.check_score()

    def point_cpu(self):
        self.clear()
        self.cpu_score += 1
        self.write_score()
        self.check_score()

    def write_score(self):
        self.write(arg=f"{self.player_score}        {self.cpu_score}", move=False, align="center", font=("Arial", 40, "bold"))

    def check_score(self):
        if self.cpu_score == 10:
            self.clear()
            self.goto(0, 0)
            self.write(arg="YOU LOSE!", move=False, align="center", font=("Arial", 40, "bold"))
        elif self.player_score == 10:
            self.clear()
            self.goto(0, 0)
            self.write(arg="YOU WIN!", move=False, align="center", font=("Arial", 40, "bold"))
