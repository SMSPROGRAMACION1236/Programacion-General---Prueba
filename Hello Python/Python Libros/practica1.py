proverb1 = "Cuando el rio suena"
proverb2 = "agua lleva"
print(proverb1 + proverb2)
print(proverb2[3])  # Es el indice 3 que es a

lyrics = 		"""	Quizás porque mi niñez
 Sigue jugando en tu playa
 Y escondido tras las cañas
 Duerme mi primer amor
 Llevo tu luz y tu olorb
 Por dondequiera que vaya			

print("rio"in proverb1)"""
print(len(lyrics))


print(lyrics.find("amor"))
print(abs(-23))
print(id(23))
print(isinstance(23, str))# Para confirmar si es un dato tipo ...
from  math  import pi
pi
print(round(pi, 1)) #rondondea 
print(round(pi, 5)) #rondondea 


### Bases

# Binaria
print(0b1010110100110101) # Lleva 0b  de binario a numero

print(bin(2)) # De numero a binario


print(int(4**(1/2)))
print(bin(2783749777777767683587638))
print(0b1001001101011110110110000010111001110111100111001000110001111011011111111000110110)

# Octal base

print(oct(73847))
print(0o220167)

# hexadecimal

print(hex(23434543))
print(0x165952f)

print(0xA)

space_odyssey = 2001
print(space_odyssey)
print(type("Good night and Good luck"))
print(type(True))

result = 10 * 3.0
print(result)


print(str(10))

thing = r"first\nsecond" # To stop \n
print(thing)

text = "My name's Thomas. I'm an architect in my mon's company"

print(text[2:9]) 
print("My" in text) # If My is in text

print(text.split())
print(text.partition(" ")) # You'd type in the argument what is the Middle to separate
print(text.count(" ")) # How many times that repeated
print(text.find("name")) # to find something
print(text.index("My")) # Similar find
print("Hello" not in text) # is like if Hello isn't in text

texting = """Hi Brenda, . Hi, Helen"""

print(texting.replace("Hi", "hello", 1))  # To replace  Hi by hello 1 time

print(text.swapcase())# The opposite of the letters

print("anf".isnumeric()) # check if it is a numeric value
print("Anf".islower())   # Check if all characters are title cased

print(f"{text=}") # to print the variable and the value

value = "hello"
print(f"{value:03}") # print 003


nul = not(None) # deny the none

if nul is  None:
  print("Wasaa")
else:
  print("Naa")


print(bool({})) # It will return False because it has no elements

