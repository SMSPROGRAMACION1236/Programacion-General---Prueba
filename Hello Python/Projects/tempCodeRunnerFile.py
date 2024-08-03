def hacer(option):
  basket ={1:1}
  while option !="leave":
    match option:
      case "1":
        key = input("Enter: ")
        value = input("Enter: ")
        basket[key]= value
        return basket
      case "2":
        key = input("Enter: ")
        del basket[key]
        return basket
  
option = str(input("Enter it: "))
print(hacer(option))