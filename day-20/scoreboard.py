from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt",mode = "r") as file:
            self.highscore = int(file.read())
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.color("White")
        self.write(f"Score : {self.score} Highscore : {self.highscore}",align="center",font = ("Arial",24,"bold"))
    def game_over_display(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=("Arial", 24, "bold"))


    def update_scorecard(self):
        self.clear()
        self.write(f"Score : {self.score} Highscore : {self.highscore}", align="center", font=("Arial", 24, "bold"))
    def reset(self):
        if self.score>self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.highscore}")
            self.score = 0
            self.update_scorecard()

    def update_score(self):
        self.score += 1
        self.update_scorecard()

