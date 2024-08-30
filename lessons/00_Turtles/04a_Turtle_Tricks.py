import random
import turtle

# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = ["red", "blue", "green", "yellow", "orange"]

def getNextColor(i):
    return colors[i % len(colors)]

window = turtle.Screen()

baseSize = 150  # the size of the black part of the star
flameSize = 80  # the length of the flaming arms

t = turtle.Turtle()
t.shape("turtle")
t.width(2) 
t.speed(0)  


for i in range(25):

    t.pencolor(getRandomColor())
    t.fillcolor(getRandomColor())  

    t.begin_fill()

    t.right(360 / 8) 
    t.forward(64)

    t.left(40) 

    t.forward(flameSize)
    t.right(170) 
    t.forward(flameSize)
    t.right(62) 
    t.forward(baseSize) 

    t.end_fill()

t.hideturtle() # Hide your turtle so you can see the pattern.
