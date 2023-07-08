"""
Cabe a recalcar que este programa o codigo fue proporcionado por BlackoBox
es decir no esta hecho por mi y por esto mismo no cuenta como un poryecto que yo mismo he hecho


"""


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


def main():
    # Get the user's input.
    a = int(input("Insertar el primer numero: "))
    b = int(input("Insertar el segundo numero: "))

    # Choose the operation.
    operation = input("Que operacion (+, -, *, /,): ")

    # Perform the operation.
    if operation == "+":
        result = add(a, b)
    elif operation == "-":
        result = subtract(a, b)
    elif operation == "*":
        result = multiply(a, b)
    elif operation == "/":
        result = divide(a, b)

    # Print the result.
    print("El resultado es: ", result)

if __name__ == "__main__":
    main()