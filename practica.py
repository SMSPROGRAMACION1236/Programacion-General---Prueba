# https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/

#Types of dates
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
Exercise 11
Imagine you'll open a bank account you'll give you 4% of interest per year. Write a program it'll start ask about the money you put into the bank account, and then calculate the money of saves in the first, second and third year, use just two decimals
"""

bank_account = int(input("Enter the money, you'll keep in this account bank: "))

account1=  bank_account *((1 + 0.04)**1)
print(f"The first year, you will pay: {round(account1, 2)}")
account2=  bank_account *((1 + 0.04)**2)
print(f"The second year, you will pay: {round(account2, 2)}")
account3=  bank_account *((1 + 0.04)**3)
print(f"The third year, you will pay: {round(account3, 2)}")

"""
Exercise 12
A bread store sell pieces of bread it's 3.49$ each one. the bread isn't of the same day, has a discount  of 60%. Write a program it counts the number of breads(which isn't of the day) selling, then the program must show the normal price, the discount to be old and the last cost """
print("The bread normally cost: 3,49")
print(3.49*(60/100))
number_breads_old = int(input("How many breads, that is old will you take: "))
number_breads_new = int(input("How many breads, that is old will you take: "))

costing_new = number_breads_new * 3.49
costing_old =  number_breads_old * 2.094
saving = 1.396 * number_breads_old
total_cost = costing_new + costing_old
print(f"You take us: {round(costing_new, 3)} dollars for the new ones and: {round(costing_old, 3)} dollars for the older ones that has a discount of 60%, you'll spend: {round(saving, 3)} dollars considering the discount and the final cost will be: {round(total_cost, 3)} dollars")



# https://aprendeconalf.es/docencia/python/ejercicios/cadenas/
#Strings

"""Exercise 1
Write a program the user, put his name and a number and print the name considering the number in different line"""


random_number = int(input("Enter a number: "))
name = str(input("What's your name? "))

for i in range(random_number):
  print(name)

"""Exercise 2
Ask to the user his full name, and do 3 prints, one all in little letter, the other with all with capital letters and the last one with the first letter in capital letter.The user can write  it how he likes"""

full_name = str(input("What is your full name: "))

print(full_name.lower())
print(full_name.upper())

print(full_name.title())


"""Exercise 3
ask to the user his name, and the count the numbers of letters that input have, it must say: <NAME> has <n> letters, where NAME must be in capital ones"""

capital_name = str(input("Enter your name: "))
capital_name = capital_name.upper()

print(f"{capital_name} has {len(capital_name)} letters ")

"""Exercise 4
A company has a phone format, that use +34 and it has two numbers as extensions(Example: +34-913724710-56)
Write a program, that delate the prefix and the extensions"""
### That i do :(
prefix_num_extension = list(str(input("Enter your full number: ")))
prefix_num_extension.pop(-16)
prefix_num_extension.pop(-15)
prefix_num_extension.pop(-14)
prefix_num_extension.pop(-13)
prefix_num_extension.pop(-1)
prefix_num_extension.pop(-2)
prefix_num_extension.pop(-3)
prefix_num_extension = ''.join(prefix_num_extension)
print(f"Your phone number without the prefix and the extensions will be: {prefix_num_extension}")


### The best form from the web
# prefix_num_extension = str(input("Enter your full number: "))
# print(f"Your phone number without the prefix and the extensions will be: {prefix_num_extension[4:-3]}")

""" Exercise 5
The user will give you a Phrase, and you will return the  reverse one"""

word = str(input("Enter a word "))

reverse_word = word[::-1]
print(reverse_word)

"""Exercise 6
make a program It ask about a word and then a vocal and print the mix of the ones and vocal must be in capital letter"""

without_vocal = str(input("Enter a word: "))
ask_vocal = str(input("Enter a vocal: "))

print(without_vocal.replace(ask_vocal, ask_vocal.upper()))

"""Exercise 7
Ask the email, and return the same one but with ceu.es."""

email_old = str(input("Enter your email: "))

ceu_es = email_old.replace("gmail.com","ceu.es.")

print(ceu_es)



"""Exercise 7
Ask the price of something in euros with two decimals and return the number of euros and decimals entered"""

euroes= input("Enter the prize: ")
parts = euroes.split(".")

print(f"It's cost {parts[0]} euros, and {parts[1]} coins")