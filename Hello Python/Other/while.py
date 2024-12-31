"""
Es un codigo en la cual cierta logica se repita, usa cierta condicion y se repita cierta cosa"""


## Con for sabemos la cantidad que se repite, pero con while la cantidad es indefinido, se ejecuta hasta que la condicion sea falsa, es decir se detiene cuando es falso


# Ejemplo de while
# cuantas lunas tiene jupiter
respuesta = int(input("Ingrese la cantidad de lunas jupiter: "))
while respuesta != 79: # Esto es la condicion que se evaluara
  ### Conjuntos de Instrucciones que se ejecutara si se  cumple la condicion
  print("La respuesta es incorrecta, intente de nuevo")
  respuesta = int(input("Ingrese la cantidad de lunas jupiter: "))
else: # opcional
  ### Conjunto de operaciones cuando la condicion no se cumple, es decir cuando sea == a 79
  print("La respuesta es correcta")
  
  
#* Uso de While como un for(iterando)

pares = [2,4,6,8]
i = 0
while i < len(pares): 
  print(pares[i]) # imprimiremos por indice 
  i += 1 # aumentando de a poco