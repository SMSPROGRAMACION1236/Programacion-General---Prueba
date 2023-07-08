### Tuples ###

my_tuple = tuple()
my_other_tuple = ()


my_tuple = (15, 1.80, "Santiago", "Sanabria", "Santiago")
my_other_tuple = (29, 60, 13,)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[4])
#print(my_tuple[-6]) Indexerror
#print(my_tuple[2])  Indexerror

print(my_tuple.count("Santiago")) # Cuenta los valores
print(my_tuple.count("Elias"))  # Sad xd
print(my_tuple.index("Sanabria")) # Para saber la posicion del dato segun el indice
### No se puede modificar una tupla, ya que es constante
#my_tuple[1] = 1.90 Error
my_sum_tuple= my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple =list(my_tuple)
print(type(my_tuple)) # Cambiar  a list, intercalado de tuple a list o vicerversa

my_tuple[4] = "SMS"
my_tuple.insert(1, "Azul")
my_tuple= tuple(my_tuple) # Cambiar a tuple
print(my_tuple)
print(type(my_tuple))
del my_tuple[2]
del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined


