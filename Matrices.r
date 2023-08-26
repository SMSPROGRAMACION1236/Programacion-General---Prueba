### Matriz ###
# Solo puedo almacenar un solo tipo de datos


A <- matrix(1:10, nrow = 5) ## 5 reglones

B = matrix(21:40, nrow =2)

C = matrix(21:30, nrow = 5)


nrow(A) # Numeros de renglones
nrow(B) # Numeros de renglones
nrow(mtcars)

ncol(A) # Numero de Columnas
ncol(B) # Numero de Columnas
ncol(C) # Numero de Columnas
ncol(mtcars) # Numero de Columnas


dim(A) # Dimension renglones y columnas

## Operaciones

A + C
A * C # Se debe de cumplir que el numero de columnas de A sea igual al numero de renglones de C
 
A[1, 2] # Extraer columna 1 renglon 2

A <- matrix(1:9, nrow = 3, byrow = TRUE) # Este ultimo parametro para llenarse de forma horizontal
A <- matrix(1:9, nrow = 3)


a <- c(4, 5, 4)
b <- c(3, 4, 4)
d <- c(8, 7, 7)

B <- rbind(a, b, d)  # Poner vectores en una matrix verticalemente


AB <- A %*% B # Division Matricial

help(dim)
t(AB)


