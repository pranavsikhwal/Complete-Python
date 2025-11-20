from turtle import Turtle
POSITIONING = [(0, 0), (-20, 0), (20, 0)]     #global are always declared in caps
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
       self.total_segment = []
    def create_snake(self):
        for _ in POSITIONING:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(_)
            self.total_segment.append(new_segment)
    def move_snake(self):
        for seg_num in range(len(self.total_segment) - 1, 0, -1):  # starting,ending and gap
            new_x = self.total_segment[seg_num - 1].xcor()
            new_y = self.total_segment[seg_num - 1].ycor()
            self.total_segment[seg_num].goto(new_x, new_y)
        self.total_segment[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.total_segment[0].heading()!= DOWN:
           self.total_segment[0].setheading(UP)

    def down(self):
        if self.total_segment[0].heading() != UP:
           self.total_segment[0].setheading(DOWN)

    def right(self):
        if self.total_segment[0].heading() != LEFT:
            self.total_segment[0].setheading(RIGHT)

    def left(self):
        if self.total_segment[0].heading() != RIGHT:
            self.total_segment[0].setheading(LEFT)


