import turtle as tt
import random
tt.speed(0.1)
tt.setup(500, 500)
t = tt.Pen()
t.goto(-250, -250)
upperEdge = tt.window_height()/2;
lowerEdge = -tt.window_height()/2;
leftEdge  = -tt.window_width()/2;
rightEdge = tt.window_width()/2;

print(upperEdge, lowerEdge, leftEdge, rightEdge)

for x in range(1000):
	position = t.position()
	if position[0] <= leftEdge:
		print('aaa')
	if position[0] >= rightEdge:
		print('bbb')
	if position[1] >= upperEdge:
		print('ccc')
	if position[1] <= lowerEdge:
		print('ddd')
		
	a = random.randint(50, 200)
	b = random.randint(20, 120)
	t.forward(a)
	t.right(b)
