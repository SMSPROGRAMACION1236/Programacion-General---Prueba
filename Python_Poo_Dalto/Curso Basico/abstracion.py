# Hand the complex, taking out the unnecessary things to the user, and creating just the important one, create a simple interface  and don't show the complex one


class Auto():
  def __init__(self):
    self.state = "Turn off"
  def turn_on(self):
    self.state = "Turn on"
    print("The car is turn on")
  def drive(self):
    if self.state == "Turn off": # if the car is turn off, first we need to turn on it
      self.turn_on()
      # if the car is already turn on
    print("Driving the car")

my_car = Auto()
my_car.drive() # here is abstraction, because the user doesn't know how it works


