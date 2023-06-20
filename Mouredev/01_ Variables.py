# variable
my_string_variable = "My string variable"
print(type("My string variable"))
print(my_string_variable)
my_bool_variable = True
print(my_bool_variable)
my_int_variable = 5
print(my_bool_variable)
 

 # Concatenacion de variables con un print


print(type (print(my_string_variable,  str (my_bool_variable),my_int_variable ))) # Tipo NoneType
my_int_to_str_variable = str(my_int_variable)
print("Esta es el valor de:" , my_bool_variable)


#funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea. !Cuidado de abusar de esta sintaxis


name, surname, alias, age = "Santiago", "Sanabria", 'SMS', float(15.2)
print("Me llamo:", name, surname,"Mi edad es:", age, "Y mi alias es" , alias)

#Inputs
firt_name = input("Cual es tu nombre? ")
age = input("Cuantos años tienes? ")
print(firt_name)
print(age)
print(type(type))


