"""Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo."""


def poli():
    opera = str(input("Ingrese la figura( triangulo, cuadrado, rectangulo): "))
    if opera == "triangulo":
        base = int(input("Ingrese su base: "))
        altura = int(input("Ingrese altura: "))
        relt1 = base * altura / 2
        print("El resultado es: ",relt1)
    elif opera == "cuadrado":
        lado = int(input("Ingrese el lado: "))
        result1 = lado**2
        print("El resultado es: ", result1)
    elif opera == "rectangulo":
        largo = int(input("Ingrese su largo: "))
        ancho = int(input("Ingrese su ancho: "))
        result2 = largo * ancho
        print("El resultado es: ", result2)

poli()