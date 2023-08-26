###Listas
# Es una estructura que puede almacenar varias estructuras vetores, matrices, dataframe, variables, listas, etc

lista_0 <-list(1, 6, 10) # Asi se declara una lista
list_1 <- list(c(1, 6, 10)) # Un solo vector con datos

list_2 <- list(c(1, 4, 6), 3:8)

list_3 <- list(mtcars, 1: 10) # Almacena una dataframe


names(list_3) <- c("Mi tabla", "Mi vector")  # Asignar nombre a una lista


list_4 <- list(caballo = 1:10, pavo= mtcars)

names(list_4) # Te muestra los nombres de los elementos
lista_vacia <- vector(mode = "list", length = 4) # Lista vacia

lista_vacia [[3]] <- c(4, 6, 987) # Añadir datos a una lista vacia



list_3[1]# Posicion 1 es data frame
list_3[2] # Es el vector posicion 2
list_3[[1]][1] # Columna 1 del dataFrame


list_3$`Mi tabla` # Consultar una columna

list_3 $`Mi tabla` [list_3$` mi tabla`$mpg == 21, ]  # Inquierda renglones y derecha columnas


length(list_4)
length(lista_vacia)
