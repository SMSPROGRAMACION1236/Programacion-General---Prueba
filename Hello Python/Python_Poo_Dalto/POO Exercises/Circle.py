
import math
class Circle:
  def __init__(self, radio) -> None:
    self. radio = radio
  def calculate_perimeter(self):
    return math.pi * radio * 2
  def calculate_area(self):
    return math.pi *  (radio ** 2)
radio = float(input("Enter radio"))
circle = Circle(radio)

print(circle.calculate_area())
print(circle.calculate_perimeter())