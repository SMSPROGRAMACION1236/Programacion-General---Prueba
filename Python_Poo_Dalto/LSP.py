## Is like Class B is subclass of A, this principle say We can use Class A in all of the situations we use Class B too.


# class Bird:
#   def __init__(self) -> None:
#     return "I'm flying"
  
# class Penguin(Bird):
#   def fly(self):
#     return "I cannot fly"


# def do_fly(bird = Bird):
#   return bird.fly()

# print(do_fly(Penguin()))


class Bird:
  pass
class FlyBird(Bird):
  def fly(self):
    return "I'm flying"
class NotFlyBird(Bird):
  pass