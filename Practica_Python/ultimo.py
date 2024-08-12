

def calculate_mean(numbers) :
  mean = 0
  for i in numbers:
    mean +=i
  return  (mean/len(numbers))
# print(calculate_mean([2,4,7,8,9,10,12,14,15,22]))






def variance_total(numbers):
  variance = 0
  mean = calculate_mean(numbers)
  for i in numbers:
    variance += (i-mean)**2
  return (variance /len(numbers )-1)
# print(variance_total([2,4,7,8,9,10,12,14,15,22]))




def desviation(numbers):
  return  (variance_total(numbers))**0.5
# print(desviation([2,4,7,8,9,10,12,14,15,22]))


def pointing(numbers):
  return(calculate_mean(numbers))/(desviation(numbers))
# print(pointing([2,4,7,8,9,10,12,14,15,22]))

def atipic(numbers):
  for i in numbers:
    if (i-(pointing(numbers))) != 2:
      print(True)
    else:
      print(False) 
atipic([2,4,7,8,9,10,12,14,15,22])