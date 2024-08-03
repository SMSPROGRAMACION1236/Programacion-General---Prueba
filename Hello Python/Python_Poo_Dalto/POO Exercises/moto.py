class motorcycle:
  motor = False
  def __init__(self, color, tuition,litres_nafta,numbers_of_wheels, brand, model, manufacturing_date, speed, weight):
    self.color = color
    self.tuition = tuition
    self.litres_of_nafta = litres_nafta
    self.numbers_of_wheels = numbers_of_wheels
    self.brand = brand
    self.model = model
    self.manufacturing_date = manufacturing_date
    self.speed = speed
    self.weight = weight
  def turn_on(self):
    if  not self.motor:
      self.motor ==True
      print("The engine is turned on.")
    else:
      print("The  engine is already running.")
  def turn_off(self):
    if self.motor:
      self.motor = False
      print("The machine was turned off")
    else:
      print("The machine was already turned off")  
car = motorcycle(1,1,1,1,1,1,1,1,1)
car.turn_on()
