## Es una funcion de order superior, es decir una funcion que acepta otra funcion como parametro
""" 
Es una funcion de manera acumulativa a los elementos de un iterable reduciendolos a un solo valor"""
from functools import reduce
#! Debemos importarlo
numeros = [1,2,3,4,5]
def sumar(num1, num2):
  return num1 + num2

total = reduce(sumar,numeros) #  suma todo para retornar solo un valor
print(total)
#* Con lambda
total = reduce(lambda num1, num2: num1 + num2, numeros)
print(total)