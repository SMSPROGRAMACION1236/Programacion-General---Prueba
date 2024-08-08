### Erro Types ###

##SytaxError

#print "Hola Mundo" Es un error
print("Hola Mundo")

## NameError

# print(name)  Es un error ya que la variable no esta declarada
ppt = "Hol"
print(ppt)

##IndexError

my_list = ["Python", "PHP", "Java", "Go", "Rust"]

print(my_list[1])
print(my_list[4])
print(my_list[-3])
# print(my_list[5]) Es un error ya que no existe el elemento 5 ya que no esta en su rango


## ModuleNotFoundError

# import matha  ya que ese modulo no existe
import math

##AtributeError

# print(math.py)   No existe el atrubuto py en el modulo math
print(math.pi)

##KeyError

my_other_dict = {"Nombre":"Santiago", "Apellido":"Sanabria", "Edad":15, 1:"Python"}

print(my_other_dict["Nombre"])
# print(my_other_dict["Apellidoo"]) es un problema con la clave ya que no existe eso

##TypeError
# print(my_list["Nombre"]) ya que es str y debe estar en comillas, es decir tiene que ser integers or slices

##ImporError

# from math import Pi   error de importar ya que debe ser pi


##ValueError

my_int = int("23")
# my_in2t = int("23 años")  Ya que int no puede tomar valores o transformar de str a int
# print(type(my_in2t)) 
print(type(my_int))

##ZeroDivisionError

print(4/2)
# print(4/0) no se puede dividir un numero entre 0 