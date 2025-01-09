# Functions has a special name start with two __ and end with two __ is like a template of a function\


class Person():
  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age
  def __str__(self) -> str: # Return a representation of an object in string
    
    
    return f"Person(name={self.name}, age={self.age})"
  def __repr__(self) -> str: # is similar __str__ but we can rebuild it in another one
    return f'Person("{self.name}", {self.age})'
  def __add__(self, other):
    new_value = self.age + other.age
    return Person(self.name + other.name, new_value)
peter = Person("Peter", 26)
mary = Person("Mary", 15)
john = Person('John', 43)

result = john + peter + mary
print(result)
print(result.name)


# print(peter) # it return as a tuple using __str__
# representation = repr(peter)
# result = eval(representation)
# print(result)
