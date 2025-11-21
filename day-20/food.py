from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        self_x = random.randint(-280, 280)
        self_y = random.randint(-280, 280)
        self.goto(self_x, self_y)
