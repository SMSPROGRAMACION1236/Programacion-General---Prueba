#0

"Hola Mundo" # Debemos de poner en comillas dobles o simples para poder hacer texto o string

hola = "lienzo"
print(type(hola))  # Saber tipo de dato

#1

'''
podemos forzar el tipo de dato poniendo : por ejemplo
''' # Es como si lo tiparamos pero igual es dinamico

locali : int = 1
locali = "Hola"
print(type(locali))  # Aqui lo volvemos a reasignar

print(len(locali)) # Saber cuantos datos caracteres existen

#2

x = 12
y = 45

z = x + y
print(z)

print(x * y) # Multiplicacion

print( y // x) # Da una division pero no admite decimales, solo enteros 
#por ejemplo 3 / 2, 1 ya que 2 x 2 es 4 y 2 x 1 es 2 y es mas cercano al 3 y 4 ya que es mas grande que 3
print(3//2)
print(x** y)  # Es la potencia es decir x elevado a y potencia

# Podemos concatenar varios string
print("Hola " + "Mundo " + "esto tiene mas de " + str(30) + " anos de antiguedad")

print(type(str(30)))  # para saber que tipo de dato es 30

# Podemos repetir palabras
print("Hola" * 5)

# Operadores Comparativos.
"""
print(3 > 4)
print( 3 <= 4)
print( 3 >= 4)
print( 3 ==  4)
print( 3 != 4)
print( 3 > 4 == 2)

"""


# x = 12
# y = 45


print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x == y)
print(x != y)
print(x != y < x)

print(len("Hola") <= len("Holaa")) # Comparar la cantidad de caracteres

s = 2
p = 4

#operadores logicos

print(s < p or s == p) # para and si o si deben de complirse todas las condiciones pero en or al menos una debe cumplirse

print( p <= s or  p == s) # En este caso ambos no son correctos por lo tanto es false unicamente sera false <--> todo es incorrecto



# Invertir o dar valor opuesto

print(not(3 > 1)) # Es decir dice lo contrario todos sabemos que 3 > 1 pero con not returna lo contrario\

#3

my_caracter : str = "My caracter"

my_other_caracter : str = "My  other caracter"

print(len(my_caracter))
print(len(my_other_caracter))

print("Hola\nhola")# en el imput all in one line pero en el output es en lineas diferentes

print("\thola\n\thola") # \t es para tabular es como la sangria, en esta ultima expresion primero pase a otra linea y luego tabular

name, school, course, language  = "santi", "nacional", 2, "spanish" # crear y asignar varias variale y sus claves


# Formas de factorizar

print("Soy {} de {} del {} y hablo {}".format(name, school, course, language))
print("Soy %s de %s del %s y hablo %s" %(name, school, course, language)) #%s es para str y %d para int
print(f"Soy {name} de {school} del {course} y hablo {language}")

# Asignar de una variable que tiene un str en varias variables

myVariable = "python"
a, b, c, d, h, n= myVariable # Es decir cada letra de python se le asigna a cada variable en este caso son letras tambien por ejemplo a = p
 
print(a)
print(b)
print(c)


print("Esto es una division") # Para dividir los outputs en el terminal

# Extraer algo especifico

yourExtraction = "Hola Mundo"  # Ponemos \t para .expandtabs()

print(yourExtraction[1])
print(yourExtraction[1:2])
print(yourExtraction[1:3])
print(yourExtraction[1:3:5])
print(yourExtraction[-2 ])
print(yourExtraction[1:]) # Es como o y las demas letras
print(yourExtraction[-5])
print(yourExtraction[-7])
  # Reverse

print(yourExtraction[::-1])  # Al reves

# Funciones 

print(yourExtraction.capitalize()) # primera letra capital
print(yourExtraction.upper()) # All in capital
print(yourExtraction.count("o")) # Cuenta la letra tenemos que pasarle si o si un caracter o sino ERROR 
print(yourExtraction.istitle()) # Si inicia con capital letter luego un  espacio y luego capital otra vez, en este caso Hola Mundo si cumple, pero no por ejemplo hola Mundo, Hola mundo, o Hola  Mundo
print("Hola mundo".istitle()) # Este ya no es
print(yourExtraction.isupper()) # Devuelve un bool si all en capital

print(yourExtraction.startswith("")) # Comprueba si empieza cn cierto caracter en este caso empieza con Ho y es True y si ponemos ho ya es false es decir diferencia las mayusculas

print(yourExtraction.casefold()) # Devuelve una versión de la cadena adecuada para comparaciones sin mayúsculas y minúsculas.
print(yourExtraction.center(20)) # Su output es el string pero con tabulacion en numeros de caracteres

print(yourExtraction.encode("utf-8")) # Regresa bytes debe tener algo a ser ejecutado que debe ser str y "utf-8" como parametro str tambien
print(yourExtraction.endswith("do"))  # Lo contrario en uso del startswith es true 
print(yourExtraction.endswith("ho"))  # Lo contrario en uso del startswith es false


print(yourExtraction.expandtabs(20))   # La variable debe tener un str con \t, lo que hace es dependiendo del parametro int, hara tabulaciones si pones 20 hara 20 tabulaciones en el output

print(yourExtraction.find("M")) # devuelve el indice en que esta el parametro str, si es mas de una letra devuelve el indice de la primera palabra y no existe ninguna coincidencia devuelve  -1 que es no existe.


print(yourExtraction.format())  # Formateo lo mismo que lo de la otra parte de este mismo codigo



mapeo = {"clave": yourExtraction}  # Es lo mismo que el format pero se usa diccionarios , luego se formata con {clave} y luego imprimis la variable en donde la impresion esta en modo de impresion. format_map() y adentro la variable en donde estan las claves : valor
cadena = "Esto es un {clave}"
print(cadena.format_map(mapeo))


# # print(yourExtraction.casefold()) 
# # print(yourExtraction.casefold()) 
# # print(yourExtraction.casefold()) 
# # print(yourExtraction.casefold()) 
