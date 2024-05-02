import turtle
import random

# Constants for the tree generation
initial_length = 150
angle = 25
scale_factor = 0.65
levels = 8

# Setup the turtle screen
screen = turtle.Screen()
screen.title("Fractal Tree Morph 4K UHD 60fps")
screen.setup(width=920, height=780)  # Set screen size

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(110)  # Set the drawing speed to maximum

# Define the function to draw the fractal tree
def draw_tree(branch_length, level):
    if level == 0:
        draw_leaf()  # Draw a leaf at the end of the branch
        return

    pen.pensize(level * 1.5)  # Vary pen size with level for a more natural look
    pen.forward(branch_length)
    pen.right(angle)
    draw_tree(branch_length * scale_factor, level - 1)
    pen.left(2 * angle)
    draw_tree(branch_length * scale_factor, level - 1)
    pen.right(angle)
    pen.backward(branch_length)

# Define a function to draw a leaf
def draw_leaf():
    pen.fillcolor(random.choice(["green", "yellow"]))  # Choose leaf color (green or yellow)
    pen.begin_fill()
    pen.circle(3)  # Draw a small circle as a leaf
    pen.end_fill()
    
    # Draw a fruit (e.g., mango) after drawing the leaf
    draw_fruit()

# Define a function to draw a fruit (e.g., mango)
def draw_fruit():
    pen.penup()
    pen.forward(10)  # Move forward a bit to position the fruit
    pen.pendown()
    pen.color("orange")  # Set fruit color (orange for mango)
    pen.begin_fill()
    pen.circle(5)  # Draw a small circle as the fruit (mango)
    pen.end_fill()
    pen.penup()
    pen.backward(10)  # Move back to the original position

# Initialize the turtle position and orientation
pen.left(90)
pen.up()
pen.goto(0, -500)  # Start drawing from a suitable position above the center
pen.down()

# Function to animate the tree morph
def animate_tree():
    for level in range(1, levels + 1):
        pen.color("brown")  # Set branch color
        pen.clear()  # Clear previous drawing
        draw_tree(initial_length, level)  # Draw the fractal tree
        
        # Reset turtle's position and orientation for next level drawing
        pen.up()
        pen.goto(0, -500)  # Move back to the starting position
        pen.setheading(90)
        pen.down()
        
        screen.update()  # Update the screen

# Start the animation
animate_tree()

# Keep the window open
turtle.mainloop()  # Run the main event loop
