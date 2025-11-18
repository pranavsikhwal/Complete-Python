import random
import turtle as tt
# import colorgram
# colors = colorgram.extract("images.jpg",30)
# rgb_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r,g,b)
#     rgb_color.append(color_tuple)
#
# print(rgb_color)

my_turtle = tt.Turtle()
tt.colormode(255)
my_turtle.speed("fastest")
my_turtle.penup()
my_turtle.hideturtle()
color_list = [(235, 231, 224), (165, 164, 160), (225, 238, 229), (240, 227, 232), (150, 98, 60), (227, 210, 89), (157, 9, 30), (199, 156, 22), (137, 164, 151), (54, 91, 156), (19, 40, 70), (220, 227, 237), (123, 163, 205), (129, 68, 98), (39, 27, 18), (85, 11, 55), (200, 137, 157), (163, 13, 4), (29, 50, 43), (197, 93, 144), (228, 166, 188), (13, 55, 128), (156, 218, 199), (63, 95, 78), (37, 82, 60), (185, 186, 208), (220, 178, 172), (187, 101, 85), (41, 74, 77), (96, 113, 171)]
my_turtle.setheading(255)
my_turtle.forward(300)
my_turtle.setheading(0)
no_of_dots = 100
for i in range(1,no_of_dots+1):
    my_turtle.dot(20, random.choice(color_list))
    my_turtle.forward(50)
    if i %10==0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)
screen = tt.Screen()
screen.exitonclick()

# print(color_list)