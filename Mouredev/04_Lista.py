 ### Lists ###
my_list = list()
my_other_list = []


print(len(my_list))

my_list = [17, 35, 62, 30, 30, 24]

print(my_list)
print(len(my_list))
my_other_list =[ 15, 1.80, "Santiago", "Sanabria"]
print(my_other_list)
print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-4])
print(my_other_list[-1])
print(my_list.count(24))
#print(my_other_list[5]) # Es un error
print(my_other_list.index("Santiago"))
age, height, name, surname = my_other_list
print(name)

print(my_list + my_other_list)


my_other_list.append("SMS") # Se agrega pero al final
print(my_other_list)

my_other_list.insert(1, " Rojo")
my_other_list.insert(1, "azul")
print(my_other_list)



my_other_list.remove("azul")
print(my_other_list)

print(my_list.pop(2))
my_pop_elem = my_list.pop(2)

del my_list[2] # Eliminar algo dependiendo del indice
print(my_list)

my_new_list = my_list.copy()

my_list.clear() # Eliminar todo
print(my_list)
print(my_new_list)

my_new_list.reverse() #Eliminar algo exacto
print(my_new_list)

my_new_list.sort() # Para ordenar
print(my_new_list)

print(my_new_list[1:3]) # Sacar dato dentro de unos determinados datos
 
my_list= "Hola Mundo"
print(my_list)
print(type(my_list))

x = [1, 2, 5, 3,6] # Prueba del pop mine
print(x.pop)
print(x)
