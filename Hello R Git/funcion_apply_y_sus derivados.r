### Funcion apply###

mtcars

mean(mtcars$mpg) # Promedio
mean(mtcars$cyl) # Promedio

resultado  <- data.frame()

promedios <- c()

for (i in colnames(mtcars)) {
  promedios <- c(promedios, mean(mtcars[, i]))
}
promedios # Calcular promedio de varias columnas en menos lineas

resultado <- rbind(promedios, resultado) # Junta promedios y resultado

colnames(resultado) <- colnames(mtcars)


#apply

apply(mtcars, MARGIN= 2, mean) # Primer parametro mtcars dataframe o matrix, MARGIN 2 es de las columns y MRGEN 1 de los renglones y el argumento final es la operacion en este caso media y debe ser sin ()



mi_matrix <- matrix(1:9, nrow= 3, ncol= 3) # Matrix de 3 x3
mi_matrix

apply(mi_matrix, 2, mean) # SUma las columnas luego  dividido 3

#lapply  # toma una lista y devuelve otro
l <-list(a= 1:10, b =11:20)


lapply(l,  mean) # Promedio
lapply(l,  sum) # Suma
class(lapply(l,  sum)) # Suma


#sapply  # Toma una lista y devuelve un vector o una matrix

s <-list(a= 1:10, b =11:20)
sapply(s, mean) # retorna un vector


#tapply # realiza operaciones de grupos


tapply(mtcars$mpg, mtcars$cyl, mean) # Del vector, en index en donde queremos agrupar y por el ultimo la operaciones y retorna un vector

tapply(mtcars$mpg, mtcars$cyl, sum)



#mapply

mapply(function(x, y){x*y}, x = 5, y =20) # Sustituye los valores y realiza sus operaciones


mapply(summary, mtcars)

