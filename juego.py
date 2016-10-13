import random
numero_al_azar = random.randint(0, 10000)
print('adivina un numero entre 0 y 10000')
for x in range(1, 16):
    numero = int(input())
    if numero == numero_al_azar:
        print('lo has adivinado a la %sª' % x)
        exit()
    elif numero < numero_al_azar:
        print('prueba mas alto')
    elif numero > numero_al_azar:
        print('prueba mas bajo')

print('Lo has intentado mas de 15 veces. El numero era el' , numero_al_azar , )