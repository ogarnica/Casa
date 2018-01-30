import turtle as t

def cuadro(x, y, color):
    t.penup()
    t.color(color)
    t.goto(x, y)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    for x in range(4):
        t.fd(30)
        t.rt(90)
    t.end_fill()

cuadro(20, 60, 'red')