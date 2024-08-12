###parte de la estructura de control
##Switch
#Significa cambio

val <- switch (4,  # Arroja el elemento de la posicion 4
  "Geeks1",
  "Geeks2",
  "Geeks3",
  "Geeks4",
  "Geeks5"
)
val  # Arroja el elemento de la posicion 4

val1 = 6
val2 = 8
val3 = "s"
result <- switch(
  
  val3,
  "s"= paste("Suma =", val1 + val2), # if val3 = s
  "r"= paste("Resta =", val1 - val2), # if val3 = r
  "d"= paste("Division =", val1 /val2), # if val3 = d
  "m"= paste("Multiplicacion =", val1 * val2), # if val3 = m
  "mo"= paste("Modulo =", val1 %% val2), # if val3 = mo
  "p"= paste("Potencia =", val1 ^ val2), # if val3 = m
  "Esta operacion no esta definida" # Si el argumento no existe
  
)

result # Es 14 ya que val3 = s por lo que busca esa letra y su operacion








use.swich <- function(x){
  
  switch (x,
    "a" = "JAJAJA",
    'e'= "JEJEJE",
    "Esa risa no esta definida" #Si no existe
  )
}

use.swich("e") # escribimos el argumento que queremos encontrar

operacion_matematica <- function(operacion, x , y){
  
  switch (operacion,
    "perro" =  x+ y,
    "gato" =  x - y,
    "Caballo" =  x *y,
    "unicornio" =  x /y,
    "Esta operacion no esta definida"
    
  )
}
operacion_matematica("perro", x= 123, y=12) # le pasamos el parametro que tiene la operacion y los valores de la x y y



funcion_maestra <- function(operacion, val1, val2){
  switch (operacion,
    
      "s"= paste("Suma =", val1 + val2), # if val3 = s
      "r"= paste("Resta =", val1 - val2), # if val3 = r
      "d"= paste("Division =", val1 /val2), # if val3 = d
      "m"= paste("Multiplicacion =", val1 * val2), # if val3 = m
      "mo"= paste("Modulo =", val1 %% val2), # if val3 = mo
      "p"= paste("Potencia =", val1 ^ val2), # if val3 = m
      "Esta operacion no esta definida" # Si el argumento no existe
  )
}
 funcion_maestra("d", val1= 9, val2 = 23)

 