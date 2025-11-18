import turtle
from turtle import Turtle,Screen
import random
my_turtle = Turtle()
my_turtle.shape("turtle")
#to draw a square
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.left(90)
# for _ in range (4):
#     my_turtle.forward(100)
#     my_turtle.right(90)

#to draw a line like _ _ _
# for _ in range (15):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()

#to draw all geomactrical shape on a same base
# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.right(90)
# for _ in range(5):
#     my_turtle.forward(100)
#     my_turtle.right(72)
# for _ in range(6):
#     my_turtle.forward(100)
#     my_turtle.right(60)
# for _ in range(7):
#     my_turtle.forward(100)
#     my_turtle.right(51.42)
# for _ in range(8):
#     my_turtle.forward(100)
#     my_turtle.right(45)
# for _ in range(9):
#     my_turtle.forward(100)
#     my_turtle.right(40)
# for _ in range(10):
#     my_turtle.forward(100)
#     my_turtle.right(36)
Color = ["Red","Blue","Orange","Yellow","Pink","Green","Grey"]
# def sides(no_of_sides):
#      for i in range(no_of_sides):
#         angle = 360/no_of_sides
#         my_turtle.forward(100)
#         my_turtle.right(angle)
# for i in range(3, 11):
#     sides(i)
#     my_turtle.color(random.choice(Color))
# generating random rgb color:
# my_turtle = turtle.Turtle()
# turtle.colormode(255)
# def random_rgb():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_rgb = (r ,g ,b )
#     return random_rgb
#
# my_turtle.pensize(15)
#my_turtle.speed("fastest")
# for _ in range(300):
#     my_turtle.color(random_rgb())
#     my_turtle.forward(30)
#     my_turtle.setheading(random.choice([90,270,180,360]))
my_turtle.speed("fastest")
def draw_circle(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        my_turtle.color(random.choice(Color))
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading()+size_of_gap)
draw_circle(5)
turtles = Screen()
turtles.exitonclick()