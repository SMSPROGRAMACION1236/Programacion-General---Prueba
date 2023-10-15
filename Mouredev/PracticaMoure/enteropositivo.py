#Escriba un programa que pida al  usuario un numero positivo y muestre en pantalla todos los  numeros impares desde 1 hasta ese numero, separados por comas.

num = int(input("Ingrese un numero: "))
if num > 0: 
  for i in range(1, num):
    if i % 2 != 0:
      print(i)
else:
  print("No es posible")

print(dir(i))
