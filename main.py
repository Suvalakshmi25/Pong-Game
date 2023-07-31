from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
screen=Screen()
ball=Ball()
l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))

scoreboard=ScoreBoard()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down, "s")
score=0
game_is_on=True
speed_ball=0.1
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    if ball.ycor()>270 or ball.ycor()<-270:
        ball.bounce_y()
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    if ball.xcor()>370:
        ball.reset_pos()
        scoreboard.l_point()
    if ball.xcor()<-370:
        ball.reset_pos()
        scoreboard.r_point()





screen.exitonclick()
