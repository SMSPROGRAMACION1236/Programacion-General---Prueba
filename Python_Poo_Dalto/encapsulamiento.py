#  The encapsulation is to protect some values, some classes, etc. We use private, very private and public  in those ones.
class MyClass:
  def __init__(self): # With _ we say it is  private
    self._private_attribute = "Value" # With _ we say it is  private
    self.__very_private_attribute = "Big Value" #With twice __ is like very private if so __ is more private than  _
    # We also can to it with functions
    def __speak(self):
      print("Hi, how are you? ")

thing = MyClass()

print(thing._private_attribute)# Without()
# print(thing.__very_private_attribute) # We cannot print it because is too private
# print(thing.__speak) # We cannot print it because is too private

### Setters and  Getters
# To into and change something in those privates ones

class Person:
  def __init__(self, name, age) -> None:
    self._name = name
    self._age = age
  # Create  a getter to  enter into the private or very private
  def get_name(self):
    return self._name
  #Create a setter to change something, with this function we  ask a new name to change it
  def set_name(self, new_name):
    self._name = new_name
    
lastname = Person("Peter", 21)
# print(lastname._age) # It is bad practice
  #print with get
name = lastname.get_name()
print(name)

# print with set

lastname.set_name("John") #Changing the namae
name = lastname.get_name()
print(name)


2:2
