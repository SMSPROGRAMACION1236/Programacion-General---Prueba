num1 = 23
num2 =12


print(num1 // num2) # the result but all in integer without decimals
print(num1 % num2) # The rest of the division 

if num1 % num2 == 0:
  print("It's perfect")
else:
  print("It's not perfect")

if num1 % num2 == 1 and num1 % num2 != 0:
  print("Ready")
elif num1 % num2 > 1 and num1 % num2 < num1 - 1:
  print("Not ready yet")

print(abs(-20)- abs(-24))
print(abs(-20--24))
if abs(-20)- abs(-24) == abs(-20--24):
  print("The multiplication is correct")
  print(abs(-20)- abs(-24))
else:
  print("There was an error with the multiplication")
