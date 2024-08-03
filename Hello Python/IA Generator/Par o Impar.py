# Pedir al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Verificar si el número es par o impar y mostrar un mensaje correspondiente
if numero % 2 == 0:
    print(numero, "es un número par.")
else:
    print(numero, "es un número impar.")