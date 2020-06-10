'''
Making a zoom background

Based on the work of Frank Stella (specifically Tahkt-I-Sulayman Variation II, 1969)
and using colors inspired by the pan flag

06/07/20
https://twitter.com/Hiitschai/status/1270087149501550592
'''

#--------------Dr. Z's Code--------------#
from turtle import *

# Create the panel to drawn on
panel = Screen()
w = 600 # width of panel
h = 600 # height of panel
panel.setup( width=w, height=w ) # 600x600 is a decent size to work on.

# Don change
panel.setworldcoordinates(0, w, h, 0)

#--------------Variables--------------#
colorList = ["#ff90aa", "#ffe1bb", "#ffdc90", "#c7edf8", "#90e6ff"]
Harry = Turtle()

#--------------Code--------------#
window = Screen()
window.clear()

Harry.pensize(50)

# First Circle
for i in range(10):
    Harry.up()
    Harry.goto( 600, 600 - ( i * 55 ) )
    Harry.color( colorList[ int( i % 5 ) ] )
    Harry.down()
    Harry.circle( 10 + ( i * 55 ) )

# Second Circle
for i in range(10):
    Harry.up()
    Harry.goto( 0, 0 - ( i * 55 ) )
    Harry.color( colorList[ int( i % 5 ) ] )
    Harry.down()
    Harry.circle( 10 + ( i * 55 ) )

# Setting up the square
Harry.up()
Harry.goto(0, 0)
Harry.color("#ffb7b7")

# Drawing the square
Harry.down()
Harry.goto( 600, 0 )
Harry.goto( 600, 600 )
Harry.goto( 0, 600 )
Harry.goto( 0, 0 )

window.exitonclick()