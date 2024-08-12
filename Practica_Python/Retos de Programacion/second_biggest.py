
# /*
#  * Reto #32
#  * EL SEGUNDO
#  * Fecha publicación enunciado: 08/08/22
#  * Fecha publicación resolución: 15/08/22
#  * Dificultad: FÁCIL
#  *


# use, sorted para para ordenar la lista, y puse como argumento reverse= True, para que se ordene de forma descendente, y por ultimo el indice 1, en donde estara el segundo numero mas grande, luego de ser ordenada.


def second_number(lista):
  return sorted(lista, reverse=True)[1] 

#implimimos, la funcion y dentro de ella le pasamos la lista de numeros

print(second_number([23, 42, 61, 13, 64]))