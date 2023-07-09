### Diccionarios ###

my_dict = dict()
my_other_dict = {}
print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Santiago", "Apellido":"Sanabria", "Edad":15, 1:"Python"}

my_dict = {
    "Nombre":"Santiago",
    "Apellido":"Sanabria",
    "Edad":"15",
    "Lenguajes":{"Python", "Go", "Rust"},
    1:1.80
}

print(my_other_dict)
print(my_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_dict["Nombre"])  #Para llamar a un valor dentro de una clave

my_dict["Nombre"] = "Mario"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle SMS"   # para añadir datos
print(my_dict)

del my_dict["Calle"]  # Eliminar un elemento especifico
print(my_dict)

print("Santiago" in my_dict)  # Busca las claves, no los valores
print("Santiage" in my_dict)
print("Apellido" in my_dict)
print(my_dict["Apellido"])

print(my_dict.items())  #un listado de cada hno de los items
print(my_dict.keys()) # Un listado de las keys
print(my_dict.values()) # Un listado de los values

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)

my_new_dict = dict.fromkeys((my_list)) # cleear un diccionario sin valores
print(my_new_dict)

my_new_dict = dict.fromkeys((my_dict)) #
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, ("Santiago", "Sanabria"))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, ["Santiago", "Sanabria"])
print(my_new_dict)

my_values= my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.keys())).keys())) 
print(list(my_new_dict.values()))
print(tuple(my_new_dict))
print(set(my_new_dict))
