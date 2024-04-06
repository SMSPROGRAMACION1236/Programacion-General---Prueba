import math as mt
print(mt.sin(10))
def sin(a):
  return mt.sin(a)
def  cos(a):
  return mt.cos(a)
  
def  tan(a):
  return mt.tan(a)
def exp(a):
  return mt.exp(a)
def log(a):
  return mt.log
def options():
  option = input("Enter the function (sin, cos, tan, exp, log)").lower()
  numbers = 0
  numbers_range_using_x = int(input("Enter the range of numbers: "))

  match  option:
    case  'sin':
      for i in range(1, numbers_range_using_x +1):
        print(f"The original number is {i} and the transformation is: {sin(i)}")
    case "cos":
      for i in range(1, numbers_range_using_x +1):
        print(cos(i))
    case "tan":
      for i in range(1, numbers_range_using_x +1):
        print(tan(i)) 
    case "exp":
      for i in range(1, numbers_range_using_x +1):
        print(exp(i)) 
    case  "log":
      for i in range(1, numbers_range_using_x +1):
        print(log(i)) 
    case _:
      print("No se puede")
options()

