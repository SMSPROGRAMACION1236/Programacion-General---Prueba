class Person:
  def __init__(self, name, age) -> None:
    self.__name = name
    self._age = age
  # Create  a getter to  enter into the private or very private
  @property # is a special decorator  to say that is a getter
  def name(self):
    return self.__name
  #Create a setter to change something, with this function we  ask a new name to change it\

  @name.setter # We use in this form to change something
  def name(self, new_name):
    self.__name = new_name
    
  @name.deleter #is a special decorator  to say that is a deleter to delete something
  def name(self):
    del self.__name

lastname = Person("Peter", 21)
# print(lastname._age) # It is bad practice
  #print with get
name = lastname.name
print(name)

lastname.name = "John"
name = lastname.name
print(name)

del lastname.name # To delate but we need the original function that have the def delate
name = lastname.name
print(name)


