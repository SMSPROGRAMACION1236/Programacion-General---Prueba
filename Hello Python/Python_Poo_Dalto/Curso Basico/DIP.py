### The high module don't depend the low module, The modules need to depend the abstractions that don't depend the Details, the details depend the abstractions the function need to depend big classes

# class Dict:
#   def check_words(self, word):
#     #Logic to check words
#     pass
# class Spell_Checker:
#   def __init__(self) -> None:
#     self.dict = Dict()
#   def check_text(self, text):
#     # we use the dict to check the text
#     pass

# The problem of the code is spell_check depend Dict it is a bad practice, because the most important class(Spell_Checker depend a small class as Dict)

### We use the good practice


from abc import ABC, abstractmethod
class Spell_Verify(ABC):
  @abstractmethod
  def verify_words(self, word):
    pass
class Dict(Spell_Verify):
  def verify_words(self, word):
  # we use the dict to check the text
    pass

class OnlineService(Spell_Verify):
  def verify_words(self, word):
    pass
class Spell_Checker:
  def verify_words():
    pass
  def __init__(self, verified) :
    self.verified = verified
  def check_text(self, text):
      # we use the verified to check the text
    pass

check = Spell_Checker(OnlineService())
#TODO Make projects using these principles


