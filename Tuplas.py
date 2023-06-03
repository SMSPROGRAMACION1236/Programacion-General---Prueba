#Como usar las tuplas
nombres = ("carlos", "marco","luz", "luis" )
numeros = (1, 2, 2, 4, 5,)
valor = (True, False, True)
comvinada = ("marco", 2, 4, True, False)

#print(len(nombres))

#Acceder a elementos de una tupla

#print(comvinada[1:3])


# Actualizar una tupla

#x = list(comvinada)
#x[3] = "Fabricio"
#comvinada = tuple(x)
#print(comvinada[3])


# Desempaquetar una tupla

#(uno, dos, tres, cuatro,cinco) = numeros
#print(uno)
#print(dos)
#print(tres)
#print(cuatro)
#print(cinco)


# Metodos de una tupla count(), index()
print(numeros.count(2))
print(numeros.index(5))