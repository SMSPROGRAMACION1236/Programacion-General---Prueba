#
"""
Crear diccionarios, apartir de operaciones a otro elementos en este caso utilizaremos listas"""
#* Normal
lista = [1,2,3,4,5]
cuadrado_dict = {}
for x in lista:
  cuadrado_dict[x] = x**2 #! Aplicar el cuadrado
print(cuadrado_dict)

#* Comprension de Disionarios

cuadrado_dict = {x:x**2 for x in lista} # es decir x:y, en donde x es la clave y  y es el valor
print(cuadrado_dict)