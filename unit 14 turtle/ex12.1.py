import turtle

window = turtle.Screen()
window.screensize(500, 500)
pen = turtle.Turtle()
pen.speed(1000)
#pen.goto(200, 200)
pen.color("Red")
for x in range(1, 1150):
    pen.backward(1000)
    pen.left(220)
turtle.done()