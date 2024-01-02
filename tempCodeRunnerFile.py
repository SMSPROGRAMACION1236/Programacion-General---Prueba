
name_to_check = str(input("Enter your name: ")).lower()
choose_sex = str(input("What are your sex: ")).lower()

if choose_sex == "female" and name_to_check[0] < "m":
  print("You'll be in the group A")

elif choose_sex == "male" and name_to_check[0] > "n":
  print("You'll be in the group A")

else:
  print("you'll be in the group B")