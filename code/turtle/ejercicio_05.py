# https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/simple_turtle_tutorial.md#beginning-with-turtle.py
from turtle import *

def blue_screen():
    bgcolor(0.7, 1.0, 1.0)

def white_screen():
    bgcolor(1.0, 1.0, 1.0)

listen()

onkeypress(blue_screen, 'space')
onkey(white_screen, 'space')

exitonclick()