""" Luego de crear los archivos con funcionalidades y tener el __init__.py, ya podemos importarlo"""

#* importacion desde un packete
from package.packagepre import middle ## para usar esta forma, la carpeta package y sus modulos no debe de estar en el mismo lugar que packagepost , tambbien podemos poner un alias con as
print(middle([1,2,2]))

#* importacion de un subpaquete
from package.sub_package1.funciones_avanzadas import  divided_by_two # Debemos traer el paquete principal y luego el subpaquete y luego la funcion.
print(divided_by_two(2))

#* Importacion de modulos de python
from math import pi
print(pi)

#* REGLAS
#* 1. Debe estar al incio del archivo, primero paquetes y luego modulos
#* 2.Primero los de python y luego los nuestros
#* 3. Debe haber una linea de espacio entre cada import