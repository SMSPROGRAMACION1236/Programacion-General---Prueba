# https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/
# Exercise 1
# print a helloworld.


print("Hello World!")

hello_world = "Hello World!"
# Exercise 2
# Create a variable it have a hello_world and then print it
print(hello_world)

"""
Exercise 3
Create a variable it asked to the user about his name, then print(Hello, <name>)"""


name = str(input("Please. Tell me your name: "))
print(f"Hi: {name}")

"""
Exercise 4
Resolve this math exercise"""

print(((3 + 2 )/(2*5))**2)
"""
Exercise 5
Ask to the user how many hours does he/she work and then print the money, she/he earn about the hours working, that one hour is 50 dollars"""


hours_worked = int(input("How many hours do you work: "))

if hours_worked == 1:
  print("You will earn 50 dollars")

print(f"You earn: {hours_worked * 50} dollars")



"""
Exercise 6
Ask one number and then add from 1 to that number the user enter, it'll be n"""
n = int(input("Enter a number: "))

add  = n*(n + 1) / 2

print(f"The add from 1 to {n} is: {int(add)}")
"""
Exercise 7
Calculate the IMC just two decimals"""

kilo = int(input("Enter your kilos: "))
hight = float(input("Enter your hight in cm: "))


imc = ((kilo / (hight **2)))

if imc >=18.5 and imc <=24.9:
  print(f"Your imc is: {round(imc, 2)} and it's normal")
elif imc >= 25 and imc <=29.9:
  print(f"Your imc is: {round(imc, 2)} and it's overweight")
else:
  print(f"Your imc is: {round(imc, 2)} and it's obesity")

"""
Exercise 8
Ask about to int numbers, then divide those two numbers a return the result and the rest"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
division = num1//num2
rest = num1 % num2

print(f"{num1} divided by {num2} is: {division} and the rest is: {rest}")

"""
Exercise 9
Calculate the capital, having the the Interest per year and the numbers of years and the money to give"""
money_giving = float(input("Please. Say me the money, you'll give: "))
time= float(input("Tell me the years of the interest: "))
interest = int(input("Tell me the interest: "))

capital  = (round(money_giving *(interest / 100 + 1)** time, 2))

print(f"You give us: {money_giving} for: {time} years, using a interest of: {interest}, you will earn: {float(capital)}")



"""Exercise 10
In a toy store the best sellers are a doll and a clown, the clown weights 112 g and the doll 75 g. Please make a program where the user put the numbers of those ones  he liked in his packages, totally, calculate the full weight that will be sent """

clown = int(input("Please, enter the numbers of clowns, you'll need: "))
doll = int(input("Please, enter the numbers of dolls, you'll need: "))

final_weight = ((clown* 112)+(doll * 75))

print(f"You'll like: {clown} clowns and: {doll} dolls and they totally will weight: {final_weight} g")

"""
Imagine you'll open a bank account you'll give you 4% of interest per year. Write a program it'll start ask about the money you put into the bank account, and then calculate the money of saves in the first, second and third year, use just two decimals
"""

bank_account = int(input("Enter the money, you'll keep in this account bank: "))

account1=  bank_account *((1 + 0.04)**1)
print(f"The first year, you will pay: {round(account1, 2)}")
account2=  bank_account *((1 + 0.04)**2)
print(f"The second year, you will pay: {round(account2, 2)}")
account3=  bank_account *((1 + 0.04)**3)
print(f"The third year, you will pay: {round(account3, 2)}")
