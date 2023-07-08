"""
calcular el precio dependiendo de las edades

"""

edad = int(input("Ingrese su edad: "))

if edad > 1 and edad < 13:
     print("No debera de pagar nada")
elif edad > 13 and edad < 18 :
    print("Debera abunar: 5 dolares")
elif edad > 18 and edad < 30:
     print("Debera abunar: 10 dolares")
elif edad > 30 and edad < 50:
    print( "Debera abunar: 20 dolares")
else:
     print("Debera abunar: 30 dolares")

