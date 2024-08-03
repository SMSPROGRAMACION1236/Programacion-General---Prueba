""" Ejemplo:
Lo que se quiere llegar hacer en este ejemplo es lograr filtrar numeros pares mayores que 0 , es decir tiene dos condiciones"""


def filtro(numeros, condicion): # condicion seria el argumento en donde ira la funcion a ser aplicada
  resultado = []
  for numero in numeros:
    if condicion(numero): # se aplica la condicion (funcion) del argumento
      resultado.append(numero) # si se cumple se pone
  return resultado
#* Las funciones que seran tomadas como argumentos en la funcion filtro  
def es_par(numero):
  return numero %2 ==0
def es_positivo(numero):
  return numero > 0
numeros = [1,2,4,5,6]


print(filtro(numeros, es_par))
print(filtro(numeros,es_positivo))
#* Existe en python una funcion especial para eso:
print(list(filter(es_par,numeros)))
print(list(filter(es_positivo, numeros)))


