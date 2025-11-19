import turtle
my_turtle = turtle.Turtle()
screen = turtle.Screen()

def move_forwards():
    my_turtle.forward(10)

def move_backwards():
    my_turtle.backward(10)
def turn_right():
    new_heading = my_turtle.heading() - 10
    my_turtle.setheading(new_heading)
def turn_left():
    new_heading = my_turtle.heading()+10
    my_turtle.setheading(new_heading)
def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()
screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
screen.onkey(turn_right,"a")
screen.onkey(turn_left,"d")
screen.onkey(clear,"c")
screen.exitonclick()

