### Son mas sencillas, y se usa muy poca veces ###
""" Se usa mucho cuandos se usan funciones de orden superior"""
# Ejemplo: Tenemos una lista de estudiantes , con el nombre y las notas

lista_estudiante = [('Edward', 4.2),
                    ('Pepe', 2.5),
                    ('Maria)', 3.1),
                    ('Carlos', 4.5)]


def returnar_nota(estudiante):
  return estudiante[1]



## sorted es una funcion de orden superior
lista_ordenada = sorted(lista_estudiante,key=returnar_nota) # Tomara la lista(primer argumento), y aplicara la funcion, en este caso tomar una nota (segundo parametro) y sorted lo ordenara
print(lista_ordenada)

#* Usando lambda
# No tiene un nombre por que es anonima
lambda estudiante:estudiante[1]  ## a:b donde a es el argumento y b es lo que hara(hace un return implicito)

lista_ordenada = sorted(lista_estudiante,key=lambda estudiante:estudiante[1],reverse=True)