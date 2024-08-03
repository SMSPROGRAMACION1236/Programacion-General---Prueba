

print(id(2))
print(id(2))

if id(2) != id(2):
  print("Different object")
else:
  print(not(not(False)))
  
print(all("ñ"))

print(id(not(not(all("3")))))