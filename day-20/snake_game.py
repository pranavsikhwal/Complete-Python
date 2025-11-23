from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width = 600,height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
my_snake = Snake()
my_food = Food()
my_score = Scoreboard()
#my_snake.create_snake()
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
    #detect collision with food:
    if my_snake.total_segment[0].distance(my_food) <15:
        my_food.refresh()
        my_snake.append()
        my_score.update_score()
    #detect collision with wall.
    if my_snake.total_segment[0].xcor()>280 or my_snake.total_segment[0].xcor()<-280 or my_snake.total_segment[0].ycor()>280 or my_snake.total_segment[0].ycor()< -280:
        my_score.reset()
        my_snake.reset_snake()
    #detect collision with tail
    for segment in my_snake.total_segment[1:]:
        # if segment == my_snake.total_segment[0]:
        #     pass
        if my_snake.total_segment[0].distance(segment)<10:
            my_score.reset()
            my_snake.reset_snake()

screen.exitonclick()
