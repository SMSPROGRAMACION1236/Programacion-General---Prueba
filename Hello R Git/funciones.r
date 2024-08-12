## Funciones de R ##

ncol(mtcars)  #Numero de columnas

summary(mtcars)

min(mtcars&mpg)

ladrar <-function(){
  print("Wuau")
  
}

ladrar()
paste("Hola", "Ximena")  # Une los strs


saludar <- function(name) {  # en los ( va  los argumentos)
  paste("hola", name)
  
}


saludar(name = " Santiago" )


programando <- function(persona) {
  paste(persona, "esta programando", "traele un cafe")
  
}
programando(persona = "Luis")



super_operacion <- function(x, u, t) {
  resultado <<- (x * u) / t # <<- asigna  una variable de forma global

 return(resultado)   # Tenemos que retonar
  
  
}

super_operacion(x = 4, u = 3, t= 6)


obtener_columna <- function(tabla, columna ){
  print(tabla[, columna])
  
}

obtener_columna(tabla = mtcars, columna = 5)



obtener_renglones <- function(tabla, hasta = 10){
  print(tabla[1:hasta, ])
}

obtener_renglones(tabla = mtcars, hasta = 10)

mtcars[1:10,]
