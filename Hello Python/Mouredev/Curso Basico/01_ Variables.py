# variable
my_string_variable = "My string variable"
print(type("My string variable"))
print(my_string_variable)
my_bool_variable = True
print(my_bool_variable)
my_int_variable = 5
print(my_int_variable)

 # Concatenacion de variables con un print

 
print(type (print(my_string_variable,  str (my_bool_variable),my_int_variable ))) # Tipo NoneType
my_int_to_str_variable = str(my_int_variable)
print("Esta es el valor de:" , my_bool_variable)


#funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea. !Cuidado de abusar de esta sintaxis


name, surname, alias, age = "Santiago", "Sanabria", 'SMS', float(15)
print("Me llamo:", name, surname,"Mi edad es:", age, "Y mi alias es" , alias)

#Inputs
"""
name = input("Cual es tu nombre? ")
#age = input("Cuantos años tienes? ")
print(name)
print(age)
print(type(type))
"""

# Cambiamos los valores
name = 55
age = "Santiage"
print(name)
print(age)
 
 #Forjamos el tipo # con el : se le puede asignar una funcion
address : str = "Mi direccion es: "
address = True
print(address)
print(type(address))
