import random

a = 0
for x in range(1, 1000001):
    double_x = random.randint(7, 20)
    a = a + double_x
a = a / 1000000
print(a)