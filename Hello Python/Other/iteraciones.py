numeros = [1,2,4,5,6]
#* Continue
"""Como ignorar una iteracion de un bucle
Todo lo que esta despues de continue sera ignorado( saltar de iteraciones)
- Se usa normalemente con condiciones
"""
for i in numeros:
  if i != 2: #? mientras que el numero no sea 2, continua iterando hasta encontrarlo e imprimirlo
    continue
  print(i)
#* break
"""
similar a continue, pero en este caso salimos del bucle, es decir no hay ignoracion, sino que desaparecemos de alli, como si fuera que es el fin del bucle
- Se usa normalemente con condiciones
"""
numeros = [1,2,4,5,6]
for i in numeros:
  print(i)
  if i == 4: # Una vez que llega a 4, salimos del bucle, por lo que solo imprime 1,2,4 y no 5 y 6
    break

#* else
""" Para saber si salimos de un bucle, es decir se ejecutara algo, tras salir del bucle
"""
numeros = [1,2,4,5,6]
for i in numeros: ## Ejecuta todo, y luego avisa al momento de salir del bucle.
  print(i)
  if i == 12:
    break
  
else:
  print("Hemos salido del bucle")