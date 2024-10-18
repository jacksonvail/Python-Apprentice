"""

Create a program that will draw a crazy pattern using the turtle.

Create lists for the path that Tina will take, the angles 
she will turn, and the colors she will use. The access those
lists to draw the pattern.

hint: all of your lists should have the same number of elements.
Review the ' Using Lists' section of the previous lesson if you need 
more help

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina
tina.shape('turtle')
tina.color("green")             # Set the shape of the turtle to a turtle
tina.speed(0)
tina.begin_fill()                           # Make the turtle move as fast, but not too fast.
tina.pencolor("green")
tina.forward(130)
tina.left(130)
tina.right(130)
tina.left(130)

for  i in range(7586):


    tina.color("red")
    tina.forward(130)
    tina.left(130)
    tina.end_fill()

turtle.exitonclick()  

