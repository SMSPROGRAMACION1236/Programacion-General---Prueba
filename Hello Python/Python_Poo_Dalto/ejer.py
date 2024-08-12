class BankAccount:
  def __init__(self,headline=13,account_number =334, balance =10000) :
    self.headline = headline
    self.balance = balance
    self.account_number = account_number
  def put_money(self):
    self.balance = int(input("Enter the money for your account"))
    return  self.balance
  def takeout_money(self):
    # self.balance = int(input("Enter the money for your account"))
    lent_money = int(input(f"How much do you want to take out from {self.balance}: "))
    return f"You've take out {lent_money} from {self.balance}, and now your balance is: {self.balance - lent_money}"
  def show_balance(self):
    return f"Your actually balance is: {self.balance}"
    
# hola = BankAccount()
# print(hola.takeout_money())
loop = True

while loop == True:
  thing = BankAccount()
  option = str(input("What would you like to do(put_money = 1,takeout_money =2 ,show_balance = 3): "))
  
  if option =="1":
    print(thing.put_money())
  elif option =="2":
    print(thing.takeout_money())
  elif option =="3":
    print(thing.show_balance())
  else:
    loop = False

import math as mt

class Fraction:
  def __init__(self, numerator, denominator):
    self.numerator = numerator
    self.denominator = denominator
  def simplify(self):
    gcd_val = mt.gcd(self.numerator, self.denominator)
    return self.numerator // gcd_val, self.denominator // gcd_val
  def adding(self,fraction1, fraction2):
    # Simplify the fractions
    # gcd_val1 = mt.gcd(fraction1.numerator, fraction1.denominator)
    # gcd_val2 = mt.gcd(fraction2.numerator, fraction2.denominator)
    # fraction1.numerator //= gcd_val1
    # fraction1.denominator //= gcd_val1
    # fraction2.numerator //= gcd_val2
    # fraction2.denominator //= gcd_val2
    # # Calculate the denominators and also the numerators
    # numerator = fraction1.numerator * fraction2.denominator + fraction2.numerator * fraction1.denominator
    # denominator = fraction1.denominator * fraction2.denominator
    # # Simplify the sum
    # gcd_val = mt.gcd(numerator, denominator)
    # numerator //= gcd_val
    # denominator //= gcd_val
    pass
def hola():
  print("Hello first")
  def bye():
    print("Bye Second")
  return bye()
hola()
    