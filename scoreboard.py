from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()
