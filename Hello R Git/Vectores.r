# Vectores

mi_vector <- c(1, 8, 5, 10)
mi_vector
class(mi_vector)

mi_vector2 <- 4: 155

length(mi_vector2)

mi_vector3 <- vector(mode = "numeric", length = 14)
mi_vector4 <- vector(mode = "logical", length = 14)
mi_vector4


hola <- c("Hola", "Como", "Estamos")
hola
# R no permite mezclar tipos de datos diferentes en vectores

mixto <- c(1, "perro", 4, 7, 2) # En este caso se cambia los numeros a string segun R
mixto


d <- c(7.1)
is.vector(d)  #Estructura de datos

is.numeric(d)  # Tipo de datos

is.character(d)

is.character(mixto)

h <- c(4, 7, 3, NA, 65, 2)  # NA = Sin valor

is.na(h)  # Para saber si un elemento esta vacio

mean(c(4, 8))  #Calcular el promedio

zinc <- c(3, 5.8, 5.6, 4.8, 5.1, 3.6, 5.5, 4.7, 5.7, 5, 5.9, 5.7, 4.4, 5.4, 4.2, 5.3, NA)
length(zinc)

zinc <- zinc[!is.na(zinc)]  # Para no hacer na.rm = TRUE

mean(zinc, na.rm = TRUE)  # PAra eliminar el NA

sd(zinc, na.rm = TRUE)  # Desviacion estandar, que tanto varia los datos en cuanto a la media o promedio

median(zinc, na.rm = TRUE) # Calcular la median


sort(zinc)

summary(zinc) # Datos y analisis

boxplot(zinc)  #Graficos
zin

hist(zinc)
plot(density(zinc), col = "blue")

c(1: 10, 8, 9, 89, 0)

c(c(1: 10, 8, 9, 89, 0),800)


rep(3, 10)  # Repetir 3 diez veces

rep(c(4, 6, 1), times = 3)  # Time repetir 3 veces

rep(c(4, 6, 1), each = 3)  # Repetir cada elemento 3 veces

seq(-2, 4, length = 10)  # Crea una frecuencia

seq(-2, 4, by = 0.5)  #Crea una secuencia empieza en 2 y termina en 4 en   0, 5

x <- 11:18
 

x[3]

x[3:6]


x[2] <- 1000  #Cambiar de valor la clave 2, pasa a tener 1000
x

rev(x)  #Voltea el vector



x[x >14 & x < 18]  # Devolver valores cumpliendo condiciones


is.element(13, x)  # Pregunta si la clave x tiene el valor 13