
import string

#0
print("\tInicio introduccion")

"Hola Mundo" # Debemos de poner en comillas dobles o simples para poder hacer texto o string

hola = "lienzo"
print(type(hola))  # Saber tipo de dato
print("\tInicio variables")
#1

'''
podemos forzar el tipo de dato poniendo : por ejemplo
''' # Es como si lo tiparamos pero igual es dinamico

locali : int = 1
locali = "Hola"
print(type(locali))  # Aqui lo volvemos a reasignar

print(len(locali)) # Saber cuantos datos caracteres existen
print("\tInicio operadores")
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
print("\tInicio Strings")
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


print(yourExtraction.index("o"))  # Como argumento debes pasarle  una letra o una palabra y te retornara su indice de la primera letra( Si es una palabra) y si no existe te dira ValueError


print(yourExtraction.isalnum())  # Para saber si es alpha numerico( si tiene letras o numeros) en este caso no es ya que Hola Mundo tiene un espacio por lo tanto --> False


print(yourExtraction.isalpha()) # Si todos los caracteres son del alfabeto no incluye numeros espacios y simbolos



print(yourExtraction.isascii())  #Este método se utiliza para comprobar si todos los caracteres en una cadena son caracteres ASCII.Caracteres ASCII son los primeros 128 caracteres en la tabla Unicode. Incluyen letras mayúsculas y minúsculas, números, símbolos de puntuación y caracteres de control. En este caso si es, pero por ejemplo la ñ no es 

print(yourExtraction.isdecimal()) # para saber si el caracter es un decimal en el sistema unicode, solo si todos los caracteres son decimales

print(yourExtraction.isdigit()) # Para saber si el caracter es un digito

jdjdj = "234"
print(jdjdj.isdigit()) #en este caso si es digit por que 234 es digito
print(jdjdj.isdecimal())

def prueba_identi(hola):
  return "Si es"

print(yourExtraction.isidentifier()) # Sirve para saber si es un identificador valido si es una variable, clase, funcion ... en este caso Hola Mundo no lo es 
print(hola.isidentifier()) # hola es ya que es una variable de una funcion

print(yourExtraction.islower()) # para saber si todo esta en minuscula,en este caso Hola Mundo tiene dos mayusculas por lo tanto no es

print(yourExtraction.isnumeric()) # Para saber si todos son numeros, Hola Mundo no es 
print(jdjdj.isnumeric())# jdjdj si es 
print(yourExtraction.isprintable())  # Si todos los caracteres son imprimibles como puede ser letras, numeros y simbolos, si tieen por ejemplo algun acento dira False

back_list = ["Hola", "Mundo"]
print(yourExtraction.isprintable()) # -> True <-> si la todos sus caracteres son imprimibles
print(yourExtraction.isspace()) # si esta vacio o sea en blanco

print(yourExtraction.join("Pa"))# para unir todos los elementos de un iterable (como una lista, tupla, etc.) en una cadena de caracteres.


# print(yourExtraction.isnumeric())
# print(yourExtraction.isnumeric())
# print(yourExtraction.isnumeric())
# print(yourExtraction.isnumeric())
# print(yourExtraction.isnumeric())




print("\tInicio listas")

# 4
  # Se puede iniciar una lista con [] o con list()
print("\tListas")
his_nummber =  [20, 3, 11, 15, 19, 81, 44]

print(his_nummber)
print(len(his_nummber)) # Cuenta cuantos elementos existe en una lista


print(type(his_nummber)) #  Imprime el tipo

print(his_nummber[1]) # Imprime  los valores poniendo como argmemto el indice  Debemos usar []

print(his_nummber[1])

print(his_nummber[3])

print(his_nummber[4])

print(his_nummber[6])
print(his_nummber[5])

print(his_nummber.count(20)) # Cuenta cuantas veces se repite un elemento en este caso solo 1 y si existe dos 20 entonces serian 2 el output

print(his_nummber.index(15)) #  Como argumento debes poner el elemnto y te retorna su indice 
print(his_nummber.index(15))
print(his_nummber.index(20))
print(his_nummber.index(81))


a, b, c, d, e, f, g = his_nummber # Asignar cada elemento de una lista a una variable cada una
print(g)
print(b)
print(c)
print(d)
print(f)
print(a)
his_other_list = [10, 23*4, 94, 54]
print(his_other_list)

print(his_nummber.append("Hola")) # Se agrega Hola a la lista al final o sea sirve para agregar elementos
print(his_nummber)

print(his_nummber.insert(1,"Ese dia"))
print(his_nummber) # Sirve para poner un elemento dentro de una lista pero esta vez si puedes elegir el lugar poniendo como primer argumento es el indice y el segundo es el elemento

print(his_nummber.remove("Hola")) # Sirve para eliminar un elemento poniendo el elemento a ser eliminado

print(his_nummber.pop(2)) ### Creo que elimina un elemento poniendo como argumento un indice
print(his_nummber.pop(3))

del his_other_list[0] # Eliminar algo con el indice del es una funcion del sistema y de varios lemguajes es decir no es propio de python
print(his_other_list)


# Tuplas
print("\tInicio Tuplas")

your_tuple = ()
print(type(your_tuple))

# Puede usarse la palabra reservada tuple() y sino se puede hacer simplemente con ()

your_tuple = ("Python", "Rust", "C#", "C", "C++", "Java", "JavaScript","Scala","TypeScript", "HTML", "CSS","Vue", "Pascal", "Lego", "R","Perl", "Swift", "kotlin","Python")

his_tuple = ("'Tigre'", "'Gato'", "'Perro'", "'Leon'", "'Caballo'")

print(your_tuple[0])# Sirve para extraer datos de la tupla, poniendo como  argumento el indice
print(your_tuple[1])
print(your_tuple[3])
print(your_tuple[8])
print(your_tuple[10])
# print(your_tuple[20]) # Es un error ya que no hay ningun elemento en el indice 20

print(your_tuple.count("Python"))# Cuenta la cantidad que se repite cierto

print(your_tuple.index("Rust")) # ponemos como argumento el elemento, y te devuelve el indice 
print(your_tuple.index("JavaScript"))
print(your_tuple.index("C#"))
print(your_tuple.index("Scala"))

# your_tuple[1] = "F# " # no se puede  asignar o sea modificar su tipo de datos 
print(type(his_tuple))
print(his_tuple)
each_tuple = your_tuple + his_tuple
print(your_tuple + his_tuple) # Podemos sumar dos tuplas
print("Tuplaaaa")
print(each_tuple[3:9])# Toma el valor desde el 3 hasta el 8
print(each_tuple[1:16]) # Del 1 al 15
print("\tSeparate")
print(each_tuple)
each_tuple = list(each_tuple)
each_tuple[1]  = "Zid" # para poner algo debemos cambiar a lista o sino  no se podra realizar
each_tuple.insert(2, "F#")
print(each_tuple)

each_tuple = tuple(each_tuple)

# each_tuple.insert(1, "234") # No se puede hacer ya que es tupla


# del each_tuple # Se elimina la tupla
print(each_tuple)

# del each_tuple[0] # No se puede hacer esto en las tuplas

print("\t Start Beginning sets")

owl_set = set()
print(type(owl_set))

kind_set ={}
print(type(kind_set)) # Al principio es un set

kind_set = {"Peter", "Hilton", "23"}
print(type(kind_set))

# Para contar los elementos

print(len(kind_set)) # Creo que no existe los indices

# Los sets no son ordenadas ni permite repeticiones
print(kind_set)
kind_set.add("SMS")
print(kind_set)
kind_set.add("SMS")
print(kind_set)
# para saber si un elemento se encuentra en el set
print("Peter" in kind_set) # Es sensible a la ortografia

## Para eliminar

# Remove : un elemento Especifico
kind_set.remove("Peter")
print(kind_set)
#Eliminar todo los elementos
kind_set.clear()
print(kind_set)
# Eliminar los elementos pero con la funcion reservada del sistema "del"
del kind_set
#print(kind_set)() # o sino error

# print(kind_set)


owl_set = {"Peter", "Johan", 21}
print(owl_set)
listation = list(owl_set) # para poder trabajar mas podemos transfomrarlo en una lista
print(type(listation))
print(listation[2]) # Un ejemplo para trabajar con indices en donde antes no se podia por ser una tupla
# Convertir de List a Set
new_set = set(listation) # Para convertirlo de nuevo
print(type(new_set))

print(new_set.add("SMS"))
print(new_set.add(223))
print(new_set)
print(owl_set)


kind_set = owl_set.union(new_set) # Para unir los sets, en este caso, no fue notorio la diferencia ya que tenia lo mismo.
print(kind_set)
print(kind_set.union(owl_set).union("C#", "Keny"))



print(kind_set)
print(owl_set)
print(new_set)
print(kind_set.difference(owl_set)) # La diferencia que existe por ejemplo, owl set no tiene 'SMS' ni 223

print(kind_set.intersection(owl_set)) # Sirve para saber que elementos tienen coincidecia, es decir si por algun o algunos elemntos se encuentran en ambas listas.

print(owl_set.discard("Peter"))  # Sirve para eliminar un elemento, debes pasar el eleemento en si, no su indice
print(owl_set)
print(owl_set.discard(21))
print(owl_set)
print(owl_set.add("Peter"))
print(owl_set.add(21))
print(owl_set)


print(owl_set.pop)


deleted_set = owl_set.pop() # Elimina un elemento, alazar ya que los sets estan desordenados,  y podemos guardar el elemento eliminado en una variable
print(owl_set)

print(deleted_set)


copy_set = new_set.copy() # Copiar un set en una variable, y las modificaciones no se afectan o sea no tienen sincronizacion.
print(copy_set)
print(owl_set)

update_set = owl_set
update_set.update({"Robert", 1643}) # Sirve para eliminar, agregar o remplazar elementos, pero no puedes camnbiar un elemento especifico por la naturaleza de los sets
print(update_set)

