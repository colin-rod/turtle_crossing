from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280,270)
        self.update_score(self.level)

    def level_up(self):
        self.level += 1
        self.update_score(self.level)

    def update_score(self,level):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align="center", font=FONT)
