import turtle

# Constants for the tree generation
initial_length = 200
angle = 20
scale_factor = 0.7
levels = 6

# Setup the turtle screen
screen = turtle.Screen()
screen.title("Fractal Tree Morph 4K UHD 60fps")
screen.setup(width=900, height=800)  # Set screen size

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(100)  # Set the drawing speed to maximum

# Define the function to draw the fractal tree
def draw_tree(branch_length, level):
    if level == 0:
        return
    pen.forward(branch_length)
    pen.right(angle)
    draw_tree(branch_length * scale_factor, level - 1)
    pen.left(2 * angle)
    draw_tree(branch_length * scale_factor, level - 1)
    pen.right(angle)
    pen.backward(branch_length)
    

# Initialize the turtle position and orientation
pen.left(90)
pen.up()
pen.goto(0, -screen.window_height() // 2 + 100)  # Start drawing from the bottom center
pen.down()

# Function to animate the tree morph
def animate_tree():
    for level in range(1, levels + 1):
        pen.color("green")  # Set tree color
        draw_tree(initial_length, level)  # Draw the fractal tree
        
        # Reset turtle's position and orientation for next level drawing
        pen.up()
        pen.goto(0, -screen.window_height() // 2 + 100)
        pen.setheading(90)
        pen.down()
        
        screen.update()  # Update the screen
        turtle.delay(0.1)  # Pause briefly before drawing next level (optional)

# Start the animation
animate_tree()

# Keep the window open
turtle.mainloop()  # Run the main event loop
