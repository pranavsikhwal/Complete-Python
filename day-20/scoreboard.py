from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.color("White")
        self.write(f"Score : {self.score}",align="center",font = ("Arial",24,"bold"))
    def game_over_display(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=("Arial", 24, "bold"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "bold"))
