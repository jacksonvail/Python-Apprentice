
""" Tash Me with a Twirl
 
Update your Tash Me Click program ( copy your old program here )
so the moustache will twirl when you click on it. 

Hint: See 08a_More Turtle Programs, section 'Click on the Turtle'
"""

... # Your code her

# Double click on this cell to copy the code

import turtle as turtle

turtle.setup(width=400, height=400)

t = turtle.Turtle()

t.shape("turtle")
t.turtlesize(stretch_wid=10, stretch_len=10, outline=4) # Make the turtle really big

def turtle_clicked(t, x, y):
    """Function that gets called when the user clicks on the turtle

    This function will make the turtle tilt 20 degrees 18 times, making a full
    circle. It is called by the turtle when the user clicks on it.

    Args:
        t (Turtle): The turtle object that was clicked
        x (int): The x coordinate of the click
        y (int): The y coordinate of the click
    """

    print('turtle clicked!')
    
    for i in range(0,360, 20): # Full circle, 20 degrees at a time
        t.tilt(20) # Tilt the turtle 20 degrees

# Connect the turtle to the turtle_clicked function
t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))


turtle.done() # Important! Use `done` not `exitonclick` to keep the window open
