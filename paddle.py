# -*- coding: utf-8 -*-
"""
Created on Wed May 25 11:26:16 2022

@author: anujg
"""
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.create_paddle(position)
    
    def create_paddle(self,position):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.pu()
        self.goto(position[0],position[1])
        
    def go_up(self):
        x,y = self.position()
        self.goto(x,y+20)
    
    def go_down(self):
        x,y = self.position()
        self.goto(x,y-20)