# DataFrame

x <- 10:1

y <- -4:5


q <- c("Hockey",
       "Football",
       "Baseball",
       "Curling",
       "Rugby",
       "Lacrose",
       "Baskeetball",
       "Tennis",
       "Cricket",
       "Soccer")
length(x)
length(y)
length(q)


mi_tabla <- data.frame(x, y, q) # Creamos el data.frame

View(mi_tabla) # Lo mismo que control clic

mtcarts

mi_tabla <-  data.frame(columna1 = x, columna2 = y, deportes = q) # Cambiar los numeros
class(mi_tabla)

mi_tabla[1:5,]  # Izquierda renglones y derecha columnas

help(mtcars) # o ?mtcars


mtcars[1:10,] # 10 primeras lineas de todas las columnas

mtcars[, 5:7] # todas las lineas de columnas 5 al 7


colnames(mtcars) # Para saber el nombre de las columnas
colnames(mi_tabla) # Para saber el nombre de las columnas


# Consultas mas avanzadas

mtcars[mtcars$cyl == 8,] # Filtrar de una propiedad en este caso los vehiculos con 8 cilindros


mtcars$cyl


mtcars[mtcars$hp > 200,] # En este caso los caballos de fuerza


(nrow(mtcars[mtcars$hp > 200, ] / nrow(mtcars)) * 100


  
head(mtcars) # Los primeros 6 registros

tail(mtcars) # Los ultimos 6 registros


ncol(mtcars) # Numero de columnas

dim(mtcars) # Primer valor numero de lineas y en el segundo el de columnas

mtcars[1,1]


mtcars[, c(1, 5)] # Para columnas exactos no en rango



mtcars[c(2,7, 23),]  # Para renglones exactos no en rango
 

mtcars # Lo mismo que mtcars[,]

mtcars [,c("mpg", "cyl")] # Filtrar por el nombre de una columna



library(tibble)

mtcars2 = tibble::rownames_to_column(mtcars, "Model")# Dar nombre a una columna sin nombre previamente


mtcars2[mtcars2$Model == "Datson 710", ] # Ahora se puede filtrar de la columna nueva

