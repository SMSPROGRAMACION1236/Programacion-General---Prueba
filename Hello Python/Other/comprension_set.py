lista = [1,2,4,5]

cuadrado_set = set()

for x in lista:
  cuadrado_set.add(x**2) # aplicamos el cuadrado
print(cuadrado_set)

#* Con comprension de sets

cuadrado_set ={x**2 for x in lista} # solo le pasamos lo que queremos que haga
print(cuadrado_set)