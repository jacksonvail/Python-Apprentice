"""
For this program, you will tell Tina the Turtle to draw 
multiple shapes.

Draw two circles, filled with different colors, 
and in different places on the screen. 

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.

"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.circle() to draw a circle, and tina.goto() to move tina to a new location
# Use tina.begin_fill(), tina.end_fill(), and tina.fillcolor() to fill in the shapes


... # Your code here
tina.begin_fill()
tina.forward(200)
tina.left(220)
tina.forward(220)
tina.left(220)
tina.forward(200)
tina.left(220)
tina.forward(200)
tina.left(220)
tina.forward(220)
tina.left(220)
tina.forward(200)
tina.left(220)
tina.pencolor("red")
turtle.exitonclick()                    # Close the window when we click on it
tina.end_fill()
tina.write("what's goodey ganglar")
# Dont forget to check in your code!