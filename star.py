import turtle


def star ( size , color ):
    boli = turtle.Pen ( )
    boli.color ( color )
    for x in range ( 1 , 19 ):
        boli.forward ( size )
        if x % 2 == 0:
            boli.left ( 175 )
        else:
            boli.left ( 225 )


rojo = (1 , 0 , 0)
azul = (0 , 0 , 1)
verde = (0 , 1 , 0)

for size in range ( 1 , 10 ):
    star ( 100 + size * 10 , rojo )
    star ( 100 - size * 10 , azul )
turtle.done ( )
