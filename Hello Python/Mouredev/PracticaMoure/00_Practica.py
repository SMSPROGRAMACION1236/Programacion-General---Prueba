## Hice solo
"""
Hice como una prueba
"""

altura = int(input("Ingrese su altura en cm: "))
peso = int(input("Ingrese su peso en kg: "))
altura= altura /100
imc = peso / (altura * altura)
resultado = imc
print("Su imc es: ", str(resultado))


if imc > 1 and imc < 20 :
    print("Delgadez")
elif imc >=20 and imc < 25:
    print("Normal")
else:
    print("sobrepeso")




