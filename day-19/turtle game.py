import turtle
import random
is_race_on = False
screen = turtle.Screen()
screen.setup(width = 500,height = 400)
user_bet = screen.textinput(title = "Make  your bet",prompt = "Which  turtle will win the race. Enter a color:")
color = ["red","orange","yellow",'green',"blue","purple"]
my_positions = [-70,-30,10,50,90,130]
all_turtles = []
for _ in range(0,6):
    my_turtle = turtle.Turtle(shape="turtle")
    my_turtle.penup()
    my_turtle.goto(-230, my_positions[_])
    my_turtle.color(color[_])
    all_turtles.append(my_turtle)

if user_bet :
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The winning turtle is of {winning_color} color")
            else:
                print(f"You lose!! The winning turtle is of {winning_color}color")

        turtle_distance = random.randint(0, 15)
        turtle.forward(turtle_distance)

screen.exitonclick()