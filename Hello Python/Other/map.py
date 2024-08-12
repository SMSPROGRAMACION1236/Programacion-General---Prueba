# Una funcion que acepta una funcion como argumento, puedo retonar una funcion o una lista
#* Map
""" 
Pasarle una lista o un iterable, y la funcion que se debe aplicar a la lista
Es decir aplica la funcionalidad a cada elemento"""
#* funcion de python
lista_nombre = ["maria","carlos"]
lista_nombre_mayus = list(map(str.upper,lista_nombre)) #! debmos convertir a un iterable en este caso lista, para que retorne lo que queremos
print(lista_nombre_mayus)
#* funcion nuestra

lista_frutas = ["banana","pera","manzana"]
sufix = "_fruta"
def agregar_sufix(fruta): #! podemos usar una lambda
  return fruta+sufix # agregamos un sufijo a cada elemento(en este caso cada fruta)
lista_fruta_sufix = list(map(agregar_sufix,lista_frutas))
print(lista_fruta_sufix)
lista_fruta_sufix = list(map(lambda fruta:fruta+sufix,lista_frutas))
print(lista_fruta_sufix)

#* con lamba