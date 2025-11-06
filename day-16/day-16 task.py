#From here we are strating OOPS
#lets start building class
# import turtle
# print(turtle.Turtle())
#Another way
# from turtle import Turtle, Screen
# harry = Turtle()
# cherry = Screen()
# harry.color("blue")
# harry.shape("turtle")
# harry.forward(500)
#
# cherry.exitonclick()
# cherry.canvheight()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align="c"
print(table)