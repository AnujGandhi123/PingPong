
from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball()
        

    def ball(self):
        self.shape("circle")
        self.color("white")
        self.pu()
        self.setheading(45)

    def move(self):
        self.forward(10)

    def bounce_y(self):
        current_heading = self.heading()
        if 0<=current_heading<=90 or 180<=current_heading<=270:
            self.setheading(current_heading - 90)
        else:
            self.setheading(current_heading + 90)

    def bounce_x(self):
        current_heading = self.heading()
        if 0<=current_heading<=90 or 180<=current_heading<=270:
            self.setheading(current_heading + 90)
        else:
            self.setheading(current_heading - 90)

    def refresh(self):
        self.bounce_x()
        self.goto(0,0)
        