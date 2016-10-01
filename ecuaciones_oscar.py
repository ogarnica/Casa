

def salir():
    resp = 0
    while True:
        resp = input('¿Quieres continuar (s/n)? ')
        r = resp.lower() in ['s', 'n']
        if r:
            break
        print('"{0}" No es la respuesta esperada. Vuelvelo a intentar'.format(resp))
    if resp == 's':
        return False
    else:
        return True


def input_float(ordinal):
    intentos = 0
    if ordinal == 1:
        mensaje = "Primer número: "
    else:
        mensaje = "Segundo número: "

    while intentos < 5:
        valor = input(mensaje)
        try:
            valor = float(valor)
            return valor
        except ValueError:
            intentos += 1
    raise ValueError("Valor incorrecto ingresado en 5 intentos")

while True:
    numero1 = input_float(1)
    numero2 = input_float(2)

    if numero1 == 0 and numero2 == 0:
        print('Hay soluciones infinitas')
    elif numero1 == 0 and numero2 != 0:
        print('No hay soluciones')
    else:
        print(numero2 / numero1)

    if salir():
        break