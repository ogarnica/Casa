import math
factores = []
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
numero = int(input('Numero a factorizar: '))
limite_bucle = math.sqrt(numero)

while numero not in primos:
    for x in primos:
        if x > limite_bucle:
            print('Es primo')
            print(int(numero))
            exit()
        else:
            resultado = numero % x
            if resultado == 0:
                numero /= x
                factores = factores + [x]
                #print(x)
                break
#print(int(numero))
factores = factores + [int(numero)]
print(factores)