### Strings ###


my_string = "My strig"
my_other_string = "My otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = " Este es un string \n con salto de linea"
print(my_new_line_string)
my_tab_string = " \t Este es un String con tabulacion"
print(my_tab_string)

my_scape_string = " \t Este es un String \n escapado"
print(my_scape_string)

#Formateo
name, surname, age = "Santiago", "Sanabria", 15

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # la f es para formatear

#Yo lo hice
a, b, c = "pepe", "alan", "Francis"
print("Eres: %s el es %s y el otro es %s" %(a, b, c))


# Desempaquetado de caracteres7
language = "python"
a, b, c, d, e, f = language # Es letra por letra
print(a)
print(b)

# Division

language_slice = language[1:3]
print(language_slice)
language_slice = language[1:]
print(language_slice)
language_slice = language[-2]
print(language_slice)
language_slice = language[0:6:2]
print(language_slice)

# Reverse
reversed_language = language [::-1]
print(reversed_language)

#Funciones
print(language.capitalize()) # 1ra letra en mayuscula
print(language.upper()) # all en mayuscula
print(language.count("t")) # cuenta la letras
print(language.isnumeric())# para saber si es un numero
print("1".isnumeric())
print(language.lower()) # Poner en minuscula
print(language.upper().isupper())

print(language.startswith("py"))
print("Py" == "py")
