# my_list = [1,2,3,4,5]
# print(len(my_list))

class Libro:
  def __init__(self, nombre, autor, paginas) -> None:
    self.nombre  = nombre
    self.autor = autor
    self.paginas = paginas
  def __str__(self) -> str: # Sirve para imprimir algo sin usar un metodo en un objeto, pudiendo imprimir directamente el objeto, y no te aparezca la direccion de pantalla
    return f"{self.nombre} escrito por {self.autor} "
  def __len__(self): # nativamente no puedes sacarle el len a un objeto puesto que no es un metodo de la clase instanciada, por lo que dentro de  clase usamos __len__ para que sea posible
    return (self.paginas)
  def __del__(self): # se puede eliminar algo sin esto, pero con esto al usar el del fuera de la clase, podremos imprimir un mensaje
    print("Se ha eliminado el objeto")
b = Libro("Aprende python desde 0","Luis",534)
print(b) #  al hacer __str__ podemos imprimir directamente con el objeto
print(len(b)) # al tener el __len__ en la clase, ya podemo usar el len

#* Se puede eliminar un objeto con del