# -*- coding: utf-8 -*-
"""
Created on Wed May 25 08:49:13 2022

@author: anujg
"""

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800,height=600)
screen.tracer(0)

#Paddle
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

#ball
ball = Ball()

#Scoreboard
score = ScoreBoard()

screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")


speed = 0.09

game_on = True
while game_on:
    time.sleep(speed)
    screen.update()
    
    #detect wall
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()

    # detect paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        speed = speed*0.5

    if ball.xcor() > 380:
        ball.refresh()
        score.left_scores()
        score.update_scores()
        speed = 0.1

    if ball.xcor() < -380:
        ball.refresh()
        score.right_scores()
        score.update_scores()
        speed = 0.1

    ball.move()
   

screen.exitonclick()