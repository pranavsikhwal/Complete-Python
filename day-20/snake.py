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
       self.create_snake()
    def create_snake(self):
        for position in POSITIONING:
            self.add_segment(position )
    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.total_segment.append(new_segment)
    def append(self):
        self.add_segment(self.total_segment[-1].position())
    def move_snake(self):
        for seg_num in range(len(self.total_segment) - 1, 0, -1):  # starting,ending and gap
            new_x = self.total_segment[seg_num - 1].xcor()
            new_y = self.total_segment[seg_num - 1].ycor()
            self.total_segment[seg_num].goto(new_x, new_y)
        self.total_segment[0].forward(MOVE_DISTANCE)
    def reset_snake(self):
        for segment in self.total_segment:
            segment.goto(1000,1000)
        self.total_segment.clear()
        self.create_snake()

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


