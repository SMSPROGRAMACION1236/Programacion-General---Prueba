### Sets ###
"""
Tiene array, vector
"""
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Santiago", "Sanabria", 15}
print(type(my_other_set))

print(len(my_other_set))  # cuenta los elementos


my_other_set.add("SMS")
print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("SMS")
print(my_other_set) # Un set no admite repetido.

print("Santiago"in my_other_set)
print("Santiage"in my_other_set)  # Para saber si se encuentra el elemento.

my_other_set.remove("Santiago")
print(my_other_set)

my_other_set.clear()   # Se elimina los elementos( todos)
print(len(my_other_set))  # len cuenta los elementos

del my_other_set
#print(my_other_set)   NameError: name 'my_other_set' is not defined

my_set = {"Santiago", "Sanabria", 15}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Go", "Rust", "Python"}
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union("C#", "C++"))  # Sirve para unir elementos en un print

print(my_new_set.difference(my_set))  # Para llamar elementos de una variable atraves de una variable
"""Tarea probar cada opcion y propiedad """