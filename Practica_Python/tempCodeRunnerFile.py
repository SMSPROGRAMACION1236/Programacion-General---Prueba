inmuebles = [
{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

def look_feature(inmuebles, budget):
  result = []
  for i in inmuebles:
    zone = i["zona"]
    metres = i["metros"]
    garage = i["garaje"]
    rooms = i["habitaciones"]
    year = i["año"]
    used_years = 2024 - year
    if zone =="A":
      price = (metres * 1000 + rooms * 5000 + garage * 15000) * (1-used_years/100)
    elif zone =="B":
      price = (metres * 1000 + rooms * 5000 + garage * 15000) * (1-used_years/100) * 1.5
    if price <=budget:
      i["precio"] = price
      result.append(i)
  return result
budget = 100000000
    
print(look_feature(inmuebles,budget))
    
      