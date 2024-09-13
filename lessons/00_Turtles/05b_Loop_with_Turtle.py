
"""
Turtles with a loop. 

This program has four identical lines of code to draw a pentagon, 
but you know you can use a loop to make the program simpler. 

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(1)                           # Make the turtle move as fast, but not too fast. 

tina.forward(150)                       # Move tina forward by the forward distance
tina.left(90)                           # Turn tina left by the left turn

tina.forward(150)                       # Continue the last two steps three more times
tina.left(90)                           # to draw a pentagon

tina.forward(150)
tina.left(90)

tina.forward(150)
tina.left(90)

tina.forward(150)
tina.left(90)                    # Close the window when we click on it
tina.left(90)
tina.forward(190)
tina.backward(170)
tina.down(190)
tina.forward(190)
tina.exitonclick()
