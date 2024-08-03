import random

palabras = ["python", "notion", "programacion", "computadora", "teclado", "inteligencia", "virtual", "asistente"]
palabra_secreta = random.choice(palabras)
letras_correctas = []
intentos_restantes = 6

print("¡Bienvenido al adivinador de palabras! Tienes que adivinar la palabra secreta.")
print("La palabra secreta tiene " + str(len(palabra_secreta)) + " letras.")

while intentos_restantes > 0:
    print("Tienes " + str(intentos_restantes) + " intentos restantes.")
    adivinanza = input("Introduce una letra: ")

    if adivinanza in letras_correctas:
        print("Ya adivinaste esa letra. Intenta con otra.")
    elif adivinanza in palabra_secreta:
        print("¡Bien hecho! La letra " + adivinanza + " está en la palabra secreta.")
        letras_correctas.append(adivinanza)
        if len(letras_correctas) == len(palabra_secreta):
            print("¡Felicidades! Adivinaste la palabra secreta: " + palabra_secreta)
            break
    else:
        print("Lo siento, la letra " + adivinanza + " no está en la palabra secreta.")
        intentos_restantes -= 1

if intentos_restantes == 0:
    print("Lo siento, se acabaron los intentos. La palabra secreta era: " + palabra_secreta)