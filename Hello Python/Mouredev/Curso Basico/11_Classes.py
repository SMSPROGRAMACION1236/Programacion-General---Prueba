### Classes ###

class MyEmptyPerson:
    pass  #se utiliza como marcador de posición, indicando que actualmente no se ha implementado código adicional dentro de la clase.


#Self se refiere a la instancia persona, que tiene una propiedad name,  == a name, y asi se le llama
print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias="Sin alias" ):  # Constructor de clase, el init lo deine
        self.full_name = f"{name} {surname} ({alias})" # Propiedad Publica
        self.__name = name  # propiedad privada

    def get_name (self):    
        return self.__name
    def walk (self):
        print(f"{self.full_name} Esta caminando")

my_person = Person("Santiago", "Sanabria")
print(my_person.full_name)

my_person.walk()

my_other_person = Person("Santiago", "Sanabria", "SMS")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Elias de Gonzales El loco de los perros"
print(my_other_person.full_name)