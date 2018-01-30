import turtle as t
import time

time.sleep(5)
t.pencolor('green')
print('esto es un juego de dibujar')
print('muevete con w, s, a, d')
print('empecemos')
try:
    while True:
        letra = input('escribe la letra')
        if letra == 'w':
            t.fd(10)
        elif letra == 's':
            t.backward(10)
        elif letra == 'a':
            t.lt(30)
        elif letra == 'd':
            t.rt(30)
        elif letra == 'q':
            t.penup()
        elif letra == 'e':
            t.pedown()
except KeyboardInterrupt:
    exit()
