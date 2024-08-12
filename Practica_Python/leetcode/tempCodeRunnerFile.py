  try:
    aleatorio:int
    if aleatorio in num:
      print("prueba con otro numero")
      aleatorio = int(input("Ingrese un numero: "))
    else:
      indice = bisect.bisect(num,aleatorio  )
      num.insert(indice, aleatorio)
      print("El  numero ya esta en la lista", indice)
  except:
    print ("No es un numero valido")