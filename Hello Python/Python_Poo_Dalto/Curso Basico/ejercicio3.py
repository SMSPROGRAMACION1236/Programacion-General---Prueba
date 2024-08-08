class Character:
  def __init__(self, name, strength, speed) -> None:
    self.name = name
    self.strength = strength
    self.speed = speed
  def __repr__(self) -> str:
    return f"{self.name} (power: {self.strength}), speed: {self.speed}"
  def __add__ (self, other_character):
    new_character = self.name + "-" + other_character.name
    new_strength = ((self.strength + other_character.strength)/2)**2
    new_speed = ((self.speed + other_character.speed)/2)**2
    return Character(new_character, new_strength, new_speed)


goku = Character("Goku", 100, 100)
print(goku)
vegeta = Character("Vegeta", 99, 99)
print(vegeta)
gogeta = goku + vegeta
print(gogeta)