#
nombre = "Santiago"
edad = 21
#* Formas de formatear un String en Python

#* Estilo C
print('Hola  "%s" tienes %d' %(nombre, edad))
## Otra forma
print('Hola  "%(nombre)s" tienes %(edad)d' %{"nombre":nombre,"edad":edad})
"""
i o d para numero entero
f floates
s string"""

#* Format
print('Hola  "{}" tienes {}'.format(nombre, edad))
### Otra forma
print('Hola  "{nombre}" tienes {edad}'.format(nombre=nombre, edad=edad))
#* F-strings

print(f'Hola  "{nombre}" tienes {edad}')
