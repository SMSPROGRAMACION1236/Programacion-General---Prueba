
age_to_enter = int(input("Enter your age: "))

if age_to_enter < 4:
  print("You can enter for free")
elif age_to_enter >=4 and age_to_enter < 18:
  print("You'll pay 5$")
elif age_to_enter >= 18 :
  print("You'll pay 10$")