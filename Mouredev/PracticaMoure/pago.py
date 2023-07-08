"""
Calcula la forma de pagar a travez de la edad
los de 13 años para abajo no deberan abunar nada
y los demas para arriva deberan abunar el costo
"""

edad =int(input("Cuantos años tienes: "))
if edad > 1 and edad < 13:
    print("Puede pasar gratis")
else:
    print("Debera abunar")
    