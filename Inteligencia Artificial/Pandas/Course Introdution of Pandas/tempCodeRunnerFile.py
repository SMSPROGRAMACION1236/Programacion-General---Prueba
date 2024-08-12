init = True
while init:
  option = input("Enter option: ")

  match option:
    case "1":
      print("Something")
    case "2":
      print("Nothing")
    case _:
      print("Hi")
      init = False
      
  