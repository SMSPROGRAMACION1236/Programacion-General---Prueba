### loops ###

# white


my_condition = 0

while my_condition < 10:  # Para cumplir una condicion  repitiendo los
    print(my_condition)
    my_condition += 2  # Para sumar en cantidades, en este caso en 2 en 2
else:  # Es opcional
    print("Mi condicion es == 10")

print("La ejecucion continua")

while my_condition < 20:
    my_condition +=1
    if my_condition == 15:
        print("Se detiene la ejecucion")
        break  # Para parar la ejecucion mediante break

    print(my_condition)

# for
my_list = [35, 24, 62, 52, 30, 30, 17]
for element in my_list:  # Para iterar elementos finitos
    print(element)

my_tuple = (15, 1.80, "Santiago", "Sanabria", "Santiago")
for element in my_tuple:
    print(element)

my_set = {"Santiago", "Sanabria", 15}
for element in my_set:
    print(element)

my_other_dict = {"Nombre":"Santiago", "Apellido":"Sanabria", "Edad":15, 1:"Python"}
for element in list(my_other_dict.values()):  # Para imprimir los valores
    print(element)

for element in my_other_dict:
    print(element)
    if element == "Edad":
        continue  # Continua
    print("Se ")
else:
    print("El bucle  para el diccionario")

for element in my_other_dict:
    print(element)
    if element == "Edad":
        break  # Para parar
    print("Se ejecuta")


print("La ejecucion continua")