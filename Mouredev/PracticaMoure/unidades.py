
# class Tiempo():
#   minutos : int
#   segundos : int
#   horas : 

def minTohour(minutos):
  return minutos / 60
  

def prin():
  
  legido = str(input("Elige:(Min, Seg, Hor): "))
  minutos= int(input("Minutos: "))
  segundos= int(input("Segundos: "))
  horas= int(input("horas: "))
  if legido == "Min":
    resultado = minTohour(minutos)
    print(dir(legido))


  print("El resultado es:", resultado)
prin()