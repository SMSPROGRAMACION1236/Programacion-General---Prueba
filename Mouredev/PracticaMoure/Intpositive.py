# Escriba un programa que pida al  usuario un numero positivo y muestre en pantalla todos los  numeros impares desde 1 hasta ese numero, separados por comas.


npositive = int(input("Ingrese un numero positivo: "))
impar= []

for i in  range (0, npositive + 1):
    if i % 2 == 1:
        impar.append(i)


print(", ".join(map(str, impar)))
