
# class Tiempo():
#   minutos : int
#   segundos : int
#   horas : 

def min_To_hour(minutos):
  return minutos / 60
def seg_To_min(segundos):
  return segundos / 60
def hour_To_min(horas):
  return horas * 60


def change():
  
  legido = str(input("Elige:(Min, Seg, Hor): "))
  print(legido)
  if legido == "Min":
    minutos =int(input("Ingrese minutos: "))
    print(minutos)
    (resultado) = min_To_hour(minutos)

  # print("El resultado es: ", resultado )
  elif legido == "Seg":
    segundos = int(input("Ingrese segundos "))
    print(segundos)
    resultado =  seg_To_min(segundos)
  elif legido == "Hor":
    horas = int(input("Ingrese horas: "))
    print(horas)
    resultado = hour_To_min(horas)
  print("El resultado es: ",resultado) 

change()
  
  # minutos= int(input("Minutos: "))
  # segundos= int(input("Segundos: "))
  # horas= int(input("horas: "))

#   if legido == "Min":
#     resultado = minTohour(minutos)
#   print("El resultado es:", resultado)
# change()