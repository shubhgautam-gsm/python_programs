import turtle

# Create a turtle object
t = turtle.Turtle()

# Move the turtle to a specific position
t.shape('turtle')
t.goto(100, 0)

# Get the current position of the turtle
current_position = t.position()

# Print the current position
print("Current position:", current_position)

# Draw a dot at the current position
t.dot(20, "blue")  # Dot size is 20 pixels, color is blue
t.stamp() 
# Move the turtle to a new position
t.shape('circle')
t.goto(150,0)

current_position = t.position()

# Print the current position
print("Current position:", current_position)
# Draw another dot at the new position
t.dot(30, "red")  # Dot size is 30 pixels, color is red

# Stamp the turtle at the current position
 # Stamp a copy of the turtle shape onto the canvas

# Move the turtle to a new position
t.goto(150, -100)
current_position = t.position()

# Print the current position
print("Current position:", current_position)
# Stamp the turtle again at the new position


# Keep the window open until it is closed by the user
turtle.done()
