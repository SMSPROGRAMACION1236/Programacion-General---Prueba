library(tidyverse)
library(magrittr)
x <- 10

if(x ==345){
  print(" Si es verdadera")
  
  
}else{
  print("Si es verdadera")
  
  
}


nombre<- "Jonni"  # R Diferencia entre mayusculas y minisculas

if (nombre == "jonni") {
  print("Hola Jonni")
}else {
  print("Donde esta Jonni")
  
}


mtcars %>%
  transform(wt = ifelse(wt > 3, "Auto Pesado", "Auto ligero") %>%
              View()

x <- 6

if (is.numeric(x)) {  # ! para poner en falso o lo contrario
  print("Esto es un numero")
  
}else{
  
  print("No es numero")}


!TRUE
!FALSE

y <- "Jonni"

if (is.character(y)) {
  print(" Es una cadena")
}else{
  
  print("No es cadena")
}

## ifelse



# El primero es la condicion el segundo sera la primera condiccion seria el if y el tercero seria si no se cumple la condicion anterior
ifelse (nombre == "Jonni", "Hi Jonni", "Dond esta Jonni")