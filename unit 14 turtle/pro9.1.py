import turtle


turtle.Screen().setup(width=600, height=400)
pen = turtle.Turtle()

pen.color("red")

angles = [0.0, 144.0, 288.0, 72.0, 216.0]

for angle in angles:
    pen.setheading(angle)
    pen.backward(200)

pen.left(144)
turtle.done()
