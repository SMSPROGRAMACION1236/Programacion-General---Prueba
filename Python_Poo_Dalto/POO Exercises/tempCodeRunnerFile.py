
class Person:
  def __init__(self, name, age, DNI) -> None:
    self.name = name
    self.age = age
    self.DIN = DNI
  def show_myself(self):
    return f"My name is {self.name} with {self.age} years old and my DNI is {self.DIN}" 
name  = str(input("Enter your name: "))
age = int(input("Type your age: "))
DNI = int(input("Enter your DNI: "))
person = Person(name, age, DNI)
print(person.show_myself())