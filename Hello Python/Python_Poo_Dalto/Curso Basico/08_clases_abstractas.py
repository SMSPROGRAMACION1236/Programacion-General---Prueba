# We cannot instantiate it, is like a recipe or recipe, por example, everyone  will use the class Person, is like a model

from abc import ABC, abstractclassmethod# it is decorate


class Person(ABC):
  @abstractclassmethod
  def __init__(self, name, age, sex, activity) -> None:
    self.name = name
    self.age = age
    self.sex = sex
    self._activity = activity
  @abstractclassmethod
  def do_activity(self):
    pass
  def introduced_myself(self):
    print(f"Hello, I'm: {self.name} with: {self.age} years old")
class Student(Person):
  def __init__(self, name, age, sex, activity) -> None:
    super().__init__(name, age, sex, activity)
  def do_activity(self):
    print(f"I'm studying: {self._activity}")
class Worked(Person):
  def __init__(self, name, age, sex, activity) -> None:
    super().__init__(name, age, sex, activity)
  def do_activity(self):
    print(f"I'm working in: {self._activity}")

# abstraction is more sa
peter = Student("peter", 13, "Male", "programming")
saint = Worked("Santiago", 23, "Male", "programming")


saint.introduced_myself()
saint.do_activity()
peter.introduced_myself()
peter.do_activity()
