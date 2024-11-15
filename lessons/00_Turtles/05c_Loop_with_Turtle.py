
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""

... # Your code here
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(190)                           # Make the turtle move as fast, but not too fast. 

tina.forward(72)                       # Move tina forward by the forward distance
tina.left(72)                           # Turn tina left by the left turn

tina.forward(72)                       # Continue the last two steps three more times
tina.left(72)                           # to draw a pentagon

tina.forward(72)
tina.left(72)

tina.forward(72)
tina.left(72)

tina.forward(72)
tina.left(72)                    # Close the window when we click on it
for i in range(1000):
    tina.forward(72)
    tina.left(72)