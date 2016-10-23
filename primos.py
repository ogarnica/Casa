valorMaximo = 10000
rango = range(2,valorMaximo)
primos = list(rango)

for idx in rango:
    esEntero = primos.count(idx)
    if esEntero:
        aBorrar = list(range(idx,valorMaximo,idx))
        tmp = aBorrar.pop(0)
        primos = [x for x in primos if x not in aBorrar]

primos.insert(0,1)
print(primos)
numPrimos = len(primos)
#print "El numero de primos en los primeros %d numeros es: %d" % (valorMaximo, numPrimos)