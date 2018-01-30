class moverse_delante:
    def __init__(self, delante):
        self.moverse_delante = delante

class moverse_detras:
    def __init__(self, detras):
        self.moverse_detras = detras

a = input('pasos delante:  ')
b = input('pasos detras:  ')
perro = moverse_delante(a)
print('me he movido',perro.moverse_delante,'pasos hacia delante')
perro = moverse_detras(b)
print('me he movido',perro.moverse_detras,'pasos hacia detras')