import turtle

window = turtle.Screen()
window.screensize(500, 500)
pen = turtle.Turtle()

# Draw vertical line
pen.left(90)  # Turn left to face upward
pen.forward(200)  # Move upward

# Draw horizontal line
pen.right(120)  # Turn right to face right
pen.forward(200)  # Move to the right

pen.right(120)  # Turn left to face upward
pen.forward(200) 
turtle.done()
