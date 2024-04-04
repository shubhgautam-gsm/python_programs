import turtle

window = turtle.Screen()
window.screensize(500, 500)
pen = turtle.Turtle()

pen.color("red")
pen.shape('turtle') # ‘arrow’, ‘classic’, ‘turtle’ or ‘circle’


angles = [0.0, 144.0, 288.0, 72.0, 216.0]

for angle in angles:
    pen.setheading(angle)
    pen.backward(200)

pen.left(144)
turtle.done()
