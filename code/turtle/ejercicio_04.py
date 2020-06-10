# https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/simple_turtle_tutorial.md#beginning-with-turtle.py
from turtle import *

def arriba():
    setheading(90)
    forward(100)

def abajo():
    setheading(270)
    forward(100)

def izquierda():
    setheading(180)
    forward(100)

def derecha():
    setheading(0)
    forward(100)

listen()

onkey(arriba, 'Up')
onkey(abajo, 'Down')
onkey(izquierda, 'Left')
onkey(derecha, 'Right')

onkey(arriba, 'w')
onkey(abajo, 's')
onkey(izquierda, 'a')
onkey(derecha, 'd')

exitonclick()