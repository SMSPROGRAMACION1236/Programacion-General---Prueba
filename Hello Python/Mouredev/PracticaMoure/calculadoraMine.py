def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def mult(a, b):
   return a * b
def divide(a, b):
   return a / b
def divideExact(a, b):
   return a // b
def delresto(a, b):
   return a % b



def main():
  a = int(input("Ingrese el primer numero: "))
  b = int(input("Ingrese el segundo numero: "))
  operacion = input("Que operacion (+, -, *, /, //, %): ")

  if operacion == "+":
     resultado = suma(a, b)
  elif operacion == "-":
     resultado = resta(a, b)
  elif operacion == "*":
     resultado = mult(a, b)
  elif operacion == "/":
     resultado = divide(a, b)
  elif operacion == "//":
     resultado = divideExact(a, b)
  elif operacion == "%":
     resultado = delresto(a, b)
  


  print("El resultado es:", resultado)

main()




