# https://twitter.com/gems_sand/status/1270313912270020608
from turtle import *
from random import randint

speed(0)
penup()
goto(-140,140)

for step in range(15):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle()
ada.color( 'red' )
ada.shape( 'turtle' )

ada.penup()
ada.goto(-160, 100)
ada.pendown()

bob = Turtle()
bob.color( 'blue' )
bob.shape( 'turtle' )

bob.penup()
bob.goto(-160, 70)
bob.pendown()

cat = Turtle()
cat.color( 'green' )
cat.shape( 'turtle' )

cat.penup()
cat.goto(-160, 40)
cat.pendown()

sam = Turtle()
sam.color( 'yellow' )
sam.shape( 'turtle' )

sam.penup()
sam.goto(-160, 10)
sam.pendown()

exitonclick()