
#https://leetcode.com/problems/search-insert-position/


import bisect

aleatorio = int(input("Ingrese un numero: "))

num = [1, 3, 5, 7, 8, 10, 13, 15, 23]


# print(num.index(5))k\


try:
  aleatorio:int
  while aleatorio in num:
    print("prueba con otro numero") 
    aleatorio = int(input("Ingrese un numero: "))
    aleatorio:int
  
  indice = bisect.bisect_left(num,aleatorio)
  num.insert(indice, aleatorio)
  print("El  numero  se puso en la lista", indice)
except:
  print ("No es un numero valido")
