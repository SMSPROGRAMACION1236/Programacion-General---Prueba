   x <- "Hola Mundo"  # Es una forma de asignar mediante <- o = o mediante una funcion
   
   assign("y", 32)  # Ponemos la variable entre "" y luego separarlo por una coma y el su respectivo valor
y

assign("name", "Santiago") ->tesoro # le asignamos a name santiago  que a su vez le asignamos a otra variable
t


exists("tesoro")
exists("name") # para comprobar que existe una variable ---> Un boleano

rm("tesoro") # Sirve para eliminar una variable
rm("y")

ls()  # Te muestra en pantalla las variables


rm(list = ls()) # para eliminar todo de una vez inicias con la funcion rm() como argumentos le pasas la lista e igualar a la funcion ls()

