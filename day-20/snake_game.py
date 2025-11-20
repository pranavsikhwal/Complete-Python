from turtle import Screen
from snake import Snake
import time
screen = Screen()
screen.setup(width = 600,height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
my_snake = Snake()
my_snake.create_snake()
screen.listen()
screen.onkey(my_snake.up,"Up")
screen.onkey(my_snake.down,"Down")
screen.onkey(my_snake.right,"Right")
screen.onkey(my_snake.left,"Left")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move_snake()
screen.exitonclick()
