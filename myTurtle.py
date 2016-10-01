import turtle

t = turtle.Pen()
a = turtle.Pen()
q = turtle.Pen()
a.up()
a.backward(200)
a.down()
# t.begin_fill()
t.color(1, 0, 0)
a.color(0, 1, 0)
for x in range(1, 19):
    t.forward(100)
    a.forward(100)
    if x % 2 == 0:
        t.left(175)
        a.left(175)
    else:
        t.left(225)
        a.left(225)

s = turtle.Pen()
s.color(0, 0, 1)
s.up()
s.left(90)
s.forward(200)
s.right(90)
s.down()
for a in range(1, 9):
    s.forward(50)
    s.left(45)
s.begin_fill()
s.circle(20)
s.end_fill()
turtle.done()