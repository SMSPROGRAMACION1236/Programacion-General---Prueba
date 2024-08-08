x <- 6
y <- "Hola"

class(x)
class(y)


#Estructura de Datos

#Vectores

s <- c(1, 6, 8, 10)


#DataFrames
tabla <- data.frame(x = 1:10, y = 11:20)

#Lista

list1 <- list(x = tabla, y = s)

#Matrices


is.matrix(as.matrix(1:10))
!is.matrix(warpbreaks)  # data.frame, NOT matrix!
warpbreaks[1:10,]
as.matrix(warpbreaks[1:10,])  # using as.matrix.data.frame(.) method

## Example of setting row and column names
mdat <- matrix(c(1,2,3, 11,12,13), nrow = 2, ncol = 3, byrow = TRUE,
               dimnames = list(c("row1", "row2"),
                               c("C.1", "C.2", "C.3")))
mdat
