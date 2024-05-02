import turtle
import random

# Constants for the tree generation
initial_length = 150
angle = 25
scale_factor = 0.65
levels = 10

# Setup the turtle screen
screen = turtle.Screen()
screen.title("Extraordinary Fractal Tree")
screen.setup(width=1200, height=800)  # Set screen size

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(0)  # Set the drawing speed to maximum

# Define a list of colors for the tree
colors = ["#663300", "#8B4513", "#A0522D", "#CD853F"]

# Define a list of leaf colors
leaf_colors = ["#228B22", "#2E8B57", "#3CB371", "#32CD32"]

# Define the function to draw the fractal tree
def draw_tree(branch_length, level):
    if level == 0:
        draw_leaf()
        return
    pen.pensize(level * 1.5)  # Vary pen size with level for a more natural look
    pen.forward(branch_length)
    pen.right(angle)
    draw_tree(branch_length * scale_factor, level - 1)
    pen.left(2 * angle)
    draw_tree(branch_length * scale_factor, level - 1)
    pen.right(angle)
    pen.backward(branch_length)

# Function to draw a leaf
def draw_leaf():
    pen.color(random.choice(leaf_colors))
    pen.begin_fill()
    for _ in range(6):
        pen.forward(5)
        pen.right(60)
        pen.forward(5)
        pen.right(120)
    pen.end_fill()

# Function to add flowers at the end of branches
def add_flower():
    pen.color("red")
    pen.begin_fill()
    pen.circle(5)
    pen.end_fill()

# Function to animate the tree morph
def animate_tree():
    for level in range(1, levels + 1):
        color = random.choice(colors)  # Choose a random color for the tree
        pen.color(color)
        draw_tree(initial_length, level)  # Draw the fractal tree
        
        # Add flowers at the end of branches for some levels
        if level % 3 == 0:
            pen.up()
            pen.forward(10)
            pen.down()
            add_flower()
            pen.up()
            pen.backward(10)
            pen.down()
        
        # Reset turtle's position and orientation for next level drawing
        pen.up()
        pen.goto(0, -screen.window_height() // 2 + 100)
        pen.setheading(90)
        pen.down()
        
        screen.update()  # Update the screen
        turtle.delay(0.01)  # Pause briefly before drawing next level (optional)

# Start the animation
animate_tree()

# Keep the window open
turtle.mainloop()  # Run the main event loop
