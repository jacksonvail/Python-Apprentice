"""
Pentagon Crazy

This program already works. Run it, then change it to make it draw a different pattern.
"""

import random
import turtle

def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

def getNextColor(i):
    return colors[i % len(colors)]

window = turtle.Screen()
window.bgcolor("black")
window.setup(width=600, height=600, startx=0, starty=0)

colors = ("red", "blue", "green", "yellow", "orange")

myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.speed(0)
myTurtle.width(1)

sides = 5
angle = 360 / sides

for i in range(760):
    if i == 100:
        myTurtle.width(3)
    if i == 200:
        myTurtle.width(4)
    myTurtle.pencolor(getNextColor(i))
    myTurtle.forward(i)
    myTurtle.right(angle + 1)

myTurtle.hideturtle()

turtle.done()
