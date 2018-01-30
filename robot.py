import turtle

turtle.setup(1000, 700)
t = turtle.Pen()
t.pensize(5)
t.speed(20)
t.penup()
t.goto(-490, -340)
t.pendown()
def movimiento():
    t.forward(995)
    t.left(90)
    t.forward(5)
    t.left(90)
    t.forward(995)
    t.right(90)
    t.forward(5)
    t.right(90)

for x in range(100):
    movimiento()
turtle.done()