class animales:
    def __init__(self, tipo):
        self.animales_tipo = tipo

perro = animales(mamifero)
print(perro.animales_tipo)
