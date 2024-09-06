"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named blake

# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()

... # Your code here

                    # Close the window when we click on it
tina.pencolor("blue")
tina.forward(50)
tina.color("blue")
tina.begin_fill()
tina.pentagon(72, steps=72)
tina.end_fill()
turtle.exitonclick()

