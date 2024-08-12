class MyClass:
  def __init__(self): # With _ we say it is  private
    self._private_attribute = "Value" # With _ we say it is  private
    self.__very_private_attribute = "Big Value" #With twice __ is like very private if so __ is more private than  _
    # We also can to it with functions
    def __speak(self):
      print("Hi, how are you? ")

thing = MyClass()

print(thing._private_attribute)# Without()
print(thing.__very_private_attribute) # We cannot print it because is too private