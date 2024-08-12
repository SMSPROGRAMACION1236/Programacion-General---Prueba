
#https://leetcode.com/problems/search-insert-position/
# Es parecido la solucion

import bisect # puedes implementar una búsqueda binaria

lista_numeros = [1, 3, 5, 7, 8, 10, 13, 15, 23,  25, 27, 29, 32, 34, 36, 38, 42, 53, 55, 61, 65, 72, 77, 81, 83, 89, 99, 101]

try:
    numero_usuario = int(input("Ingresa un número: "))
    while numero_usuario in lista_numeros: 
        # Con esto insistirá al usuario a ingresar un número que no está en la lista
        print("Prueba con otro número") 
        numero_usuario = int(input("Ingresa otro número: "))
    
    indice = bisect.bisect_left(lista_numeros, numero_usuario)  # Con esto te podrá dar el índice cercano más bajo posible
    lista_numeros.insert(indice, numero_usuario) # para insertar el nuevo valor, en la lista original dada ya su índice
    print(f"El número se puso en la lista {indice}")
    print(f"Ahora la lista está conformada por: {lista_numeros}") 
except ValueError: 
    print("No es un número válido") # Si se ingresa un dato != int