## Don't make  an effort to  depend intefaces we don't use

from abc import ABC, abstractmethod

class HardWorking(ABC):
  @abstractmethod
  def working(self):
    pass
class Eater:
  @abstractmethod
  def eat(self):
    pass
class Sleeper:
  @abstractmethod
  def sleep(self):
    pass

class Human(HardWorking, Eater, Sleeper):
  def eat(self):
    print("The human is eating")

  def working(self):
    print("The human is working")
  def sleep(self):
    print("The human is sleeping")

class Robot(HardWorking):
  def working(self):
    print("The Robot is working")



robot = Robot()
robot.working()


human = Human()
human.eat()
human.sleep()
human.working()