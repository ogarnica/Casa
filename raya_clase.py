import turtle as t

t.speed(0)
t.ht()


class jugador:
    def __init__(self):
        self.name = input('como te llamas? ')
        self.fichas = []
        self.color = input('color(red, blue): ')

    def jugar(self, tamano_tablero):
        print(self.name + ' eliges: ')
        fila = int(input('   Fila: '))
        columna = int(input('   Columna: '))
        pos = (((fila-1)*tamano_tablero) + columna)-1
        self.fichas.append(pos)
        return pos

    def linea(self, salto):
        for y in self.fichas:
            ganar = 1
            fichas_en_linea = []
            for i in range(1, 3):
                ficha_kk = i * y + salto
                if ficha_kk > 15:
                    ficha_kk = ficha_kk - 16
                fichas_en_linea.append(ficha_kk)
            #     ficha_kk = i*y+salto
            #     if ficha_kk < 16 or ficha_kk not in frontera
            #         fichas_en_linea.append(ficha_kk)
            # if len(fichas_en_linea) != 2:
            #     ganar = 0
            #fichas_en_linea.append(y + salto)
            #fichas_en_linea.append(y + 2 * salto)
            for q in fichas_en_linea:
                if q not in self.fichas:
                    ganar = 0
            if ganar == 1:
                return ganar
        return ganar


    def ganar(self, tamano_tablero):
        return self.linea(1) or self.linea(tamano_tablero) or self.linea(tamano_tablero+1) or self.linea(tamano_tablero-1)

class cuadrado:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.ocupado = 0

    def set_jugador(self, objjugador):
        self.ocupado = objjugador

    def setCoord(self, x1, y1):
        self.x = x1
        self.y = y1

    def dibujar(self):
        t.penup()
        if self.ocupado == 0:
            t.color('black', 'white')
        else:
            t.color(self.ocupado.color)
        t.goto(self.x, self.y)
        t.pendown()
        t.setheading(0)
        t.begin_fill()
        for x in range(4):
            t.fd(30)
            t.rt(90)
        t.end_fill()


class tablero:
    def __init__(self):
        self.tamano_tablero = int(input('tamano: '))
        self.cuadrados = [cuadrado() for count in range(self.tamano_tablero * self.tamano_tablero)]
        x = 0
        y = 0
        n = 0
        for k in self.cuadrados:
            k.setCoord(x, y)
            x += 30
            n += 1
            if n == self.tamano_tablero:
                x = 0
                y -= 30
                n = 0
        self.dibujar()
        self.fronteras_vert = []
        self.fronteras_horz = self.tamano_tablero**2-1
        for i in range(0, self.tamano_tablero-1):
            self.fronteras_vert.append(self.tamano_tablero*i)

    def dibujar(self):
        for k in self.cuadrados:
            k.dibujar()


class partida:
    def __init__(self):
        self.tablero = tablero()
        num_jugadores = int(input('jugadores: '))
        self.jugadores = [jugador() for count in range(num_jugadores)]

    def jugar(self):
        while True:
            for k in self.jugadores:
                posicion = k.jugar(self.tablero.tamano_tablero)
                self.tablero.cuadrados[posicion].set_jugador(k)
                self.tablero.cuadrados[posicion].dibujar()
                k.ganar(self.tablero.tamano_tablero)
                if k.ganar(self.tablero.tamano_tablero):
                    print('Jugador '+k.name+' ha ganado!')
                    exit()


partida1 = partida()
partida1.jugar()
