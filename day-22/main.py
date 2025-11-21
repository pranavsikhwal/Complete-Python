from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800,height = 600)
screen.title("Pong Game")
screen.tracer(0)
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
my_ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


is_game_on = True
while is_game_on:
    screen.update()
    my_ball.move()
    time.sleep(my_ball.move_speed)
    #detect collision with wall
    if my_ball.ycor()>280 or my_ball.ycor()<-280:
        my_ball.y_bounce()
    #detect collision with paddles
    if my_ball.distance(r_paddle)<50 and my_ball.xcor()>320 or my_ball.distance(l_paddle)<50 and my_ball.xcor()< -320:
        my_ball.x_bounce()
    #to reset the game after ball misses by paddles
    if my_ball.xcor()>380:
        my_ball.reset_game()
        scoreboard.l_increase_score()
    if my_ball.xcor() < -380:
        my_ball.reset_game()
        scoreboard.r_increase_score()
    Scoreboard()




screen.exitonclick()
