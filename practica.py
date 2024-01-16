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



"""Exercise 8
Ask the price of something in euros with two decimals and return the number of euros and decimals entered"""

euro= input("Enter the prize: ")
parts = euro.split(".")

print(f"It's cost {parts[0]} euros, and {parts[1]} coins")




"""Exercise 9
Ask the user his date of born, in dd/mm/aaaa  and print the day, the month and the year"""

date_of_born = str(input("Enter your date of born: "))
pieces = date_of_born.split("/")

print(pieces[0])
print(pieces[1])
print(pieces[2])


"""Exercise 10
Write a program asking about the products, separate by comas and print each product in a different line"""

products = str(input("What are the products: "))

show_products = products.split(",")

for word in show_products:
  print(word)
pieces

"""Exercise 11
Ask about the name of a product, its price and the number of units and print a string with the product name, its  unit price with 8 digits that is's integer and two decimals, the number of unit with 3 digits and the total cost with 8 digits in integer and two decimals"""


product_name = str(input("Enter the product name: "))

many = input(f"How many of {product_name} do you like: ")
many = int(many) 
each_unit = input("Enter the unit prize: ")
each_unit = int(each_unit)
total_many = many * each_unit 

each_unit = "{:.2f}".format(each_unit)
each_unit = each_unit.zfill(11)

total_many = "{:.2f}".format(float(total_many))
total_many = total_many.zfill(11)

many = str(many) 
many = many.zfill(3)
print(f"You'll buy: {product_name} you'll have: {many} units that each one cost: {each_unit} dollars, totally is going to be: {total_many}")

# https://aprendeconalf.es/docencia/python/ejercicios/condicionales/
#conditionals

"""Exercise 1
Ask the user his age and print if he is older or not"""

age = int(input("How old are you: "))

if age < 18:
  print("You are younger than 18 years old.")
else:
  print("You are older than 18 years old.")
""" Exercise 2
Check if the password is correct where the password is 'password'"""

put_password = "password"
check_password = str(input("Enter your password: "))

if check_password == put_password:
  print("It is")
else:
  print("It isn't")


"""Exercise 3
Ask the user two numbers divided  and if the divisor is 0 print a error"""

n1 = int(str(input("Enter the dividing: ")))
n2 = int(str(input("Enter the divisor: ")))

if n2 == 0:
  print("Error")
else:
  print(int(n1 /n2))
  
  
"""Exercise 4
ask the user a number a check if it is pair or the opposite"""

pair = int(input("Enter a number: "))

if pair % 2 == 0:
  print("it's pair")
else:
  print("It's odd")
"""Exercise 5
The user need to know if the persons can have a tribute just if they earn more 1000 dollars every month and they are older that 16 years. Please check"""


pre_tribute = int(input("how much do you earn in this month: "))
get_year =int(input("How old are you: "))

if pre_tribute >= 1000 and get_year > 16:
  print("You need to tribute")
else:
  print("you don't need to tribute yet")
"""
Exercise 6
There are two groups the group A with women with their first name letter before M and the men with his first name letter after N and the Group B is the rest"""

name_to_check = str(input("Enter your name: ")).lower()
choose_sex = str(input("What are your sex: ")).lower()

if choose_sex == "female" and name_to_check[0] < "m":
  print("You'll be in the group A")

elif choose_sex == "male" and name_to_check[0] > "n":
  print("You'll be in the group A")

else:
  print("you'll be in the group B")

"""
Exercise 7
Knowing the table of fax, put the income in the different groups of fax
"""

income = float(input("Enter your income per year: "))

if income < 10000:
  print(f"Your fax is 5% and you'll pay: {income * 5 / 100} dollars ")
elif income >= 10000 and income < 20000:
  print(f"Your fax is 15% and you'll pay: {income * 15 / 100} dollars ")
elif income >=20000 and income < 35000:
  print(f"Your fax is 20% and you'll pay: {income * 20 / 100} dollars ")
elif income >= 35000 and income < 60000:
   print(f"Your fax is 30% and you'll pay: {income * 30 / 100} dollars ")
else:
   print(f"Your fax is 45% and you'll pay: {income * 45 / 100} dollars ")

"""
Exercise 8
In a company the clerks have been checked, everyone has points it started in 0.0 and i can increase, they can have points, 0.0, 0.4, 0.6 o mas, but without any values between those ones, the money earn in each level is 2.400 dollars. Write a program it read the points given and the quantity of money earning"""

point = float(input("Enter your points: "))

quantity_of_money = 2400 
unaccepted =  0.0
accepted = 0.4
too_good = 0.6


if point == unaccepted :
  level = "unaccepted"
  print(f"you are in level: {level} and you'll earn: {unaccepted * quantity_of_money}")
elif point == accepted:
  level = "accepted"
  print(f"you are in level: {level} and you'll earn: {accepted * quantity_of_money}")
elif point >= too_good:
  level = "too good"
  print(f"you are in level: {level} and you'll earn: {point * quantity_of_money}")
else:
  print("try again")
  
"""
Exercise 9
A company that is has a playground needs to calculate the price it must sell to enter there, it need to ask the age of the client and show the price of the entering. if the client is lower than 4 years can enter free, if it has between 4 and 18 years old must pay 5$ and if it is older than 18 years it'll pay 10$"""

age_to_enter = int(input("Enter your age: "))

if age_to_enter < 4:
  print("You can enter for free")
elif age_to_enter >=4 and age_to_enter < 18:
  print("You'll pay 5$")
elif age_to_enter >= 18 :
  print("You'll pay 10$")
"""Exercise 10
A shop of pizza, has a vegetable pizza and a meat pizza each of them has their own Ingredients, and write if the user choose the vegetable one or the meat one and show the ingredients"""

kind_of_pizza = str(input("Enter the kind of pizza:(Meat/Vegetable): ")).lower()

if kind_of_pizza == "meat":
  ingredients_meat = str(input("Choose the ingredient:(pimiento/tofu)"))
  print(f"You choose a meat one, it have mozzarella, tomato, {ingredients_meat}")
elif kind_of_pizza == "vegetable":
  ingredient_vegetable = str(input("Choose the ingredient:(peperoni/ham/salmon): "))
  print(f"You choose a vegetable one, it have mozzarella, tomato, {ingredient_vegetable}")


### Loops ###
#https://aprendeconalf.es/docencia/python/ejercicios/bucles/

"""Exercise 1
Ask the user a word and print ten times"""

word_loop = str(input("Enter a word: "))

for i in range(10):
  print(word_loop)

"""Exercise 2 
Ask the user his age and show all the ages he has been(from year 1)"""


age_for_loop = int(input("Enter your age: "))

for i in range(1, age_for_loop +1):
  print(i)

"""Exercise 3
Write a  program ask a  positive number and show all the numbers odds from 1 to that numbers with comas"""



num_for_loop = int(input("Enter a positive number: "))


# while num_for_loop > 0:
#   # print("It's negative")
#   # num_for_loop = int(input("Enter a positive number: "))
#   print(num_for_loop % 2  == 0)


for i in range(1, num_for_loop):
  if i % 2 == 0:
    print(i, end=",")
"""Exercise 4
Write a program ask the user a positive number and show by screen the count back from the number to 0 by comas"""

num_back = int(input("Enter a positive number"))
# while num_back >= 0:
#   print(num_back, end=",")
#   num_back = num_back - 1


"""Exercise 5
Write a program ask the quantity to income, the income in year the numbers of years, and show the capital had in the income each year during it"""
amount = float(input("Quantity to income "))
interest = float(input("¿faz of interest? "))
years = int(input("Years?"))
for i in range(years):
    amount *= 1 + interest / 100 
    print("Capital after " + str(i+1) + " years: " + str(round(amount, 2)))
    # TODO: Complete by myself it


"""
Exercise 6
Write a program ask a integer number ans show a right triangle with hight of the input
"""

number_for_triangle = int(input("Enter a number"))
sign = ""
for i in range (1, number_for_triangle + 1):
  sign += "*" * 1
  print(sign)
"""
Exercise 7
Write a program it show the times table"""

for i in range(1, 11):
  for k in range(0, 11):
    print("{:3d}".format(k * i), end=" \t")
  print("")
"""
Exercise 8
Write a program that ask the user a positive number and show a triangle with from 1 to that number in the output but just the odd ones """


triangle_for_number = int(input("enter a positive"))

while triangle_for_number < 0:
  print("It's not positive")
  triangle_for_number = int(input("enter a positive"))


def print_number(triangle_for_number):
  for t in range(1, triangle_for_number+1, 2):
    for h in range(t, 0, -2):
      print(h, end="")
    print()
print_number(triangle_for_number)
"""
Exercise 9
Create a variable, it has 'password' , ask to the user about it since the password will be correct"""

loop_password = "password"
user_password = str(input("Type your password: "))

while user_password != loop_password:
  print("Your password is incorrect")
  user_password = str(input("Type your password: "))
  
else:
  print("Your password is correct")

"""Exercise 10
Write a program that ask the user a number and show if it is  a prime number"""

prime_number = int(input("Type a  positive number: "))
verify = "V"
init = 2

while prime_number <0:
  print("This is not a valid input")
  prime_number=int(input("Type a positive number"))
else:
  while ((verify == "V") and(init < prime_number)):
    if (prime_number % init )== 0 :
      verify ="F"
    else:
      init +=1
  if verify=="V":
    print("It's prime")
  else:
    print("It's not prime")
    
"""Exercise 11
Write a program that print the letters of the given string but reverse the  letters

"""

string_for_reverse = str(input("Enter a string: "))

for i in range(len(string_for_reverse) - 1, -1, -1):
  print(string_for_reverse[i])

"""Exercise 12
Write a program, ask a phrase and a letter, and return the number of letters into the phrase"""

import re
phrase = input("Enter a phrase: ")
letter = input("Enter a letter: ")
alphabets = re.findall("[a-zA-Z]", phrase) # extract all the alphabets from the phrase
count = len([c for c in alphabets if c == letter]) # count the number of alphabets that match the letter
print("The number of", letter, "in the phrase is", count)

"""Exercise13
Write a program, that repeat the word entering and stop the program if it is leave"""

while True:
  expression = str(input("Enter something: ")).lower()
  if expression == "leave":
    break
  print(expression)
### Lists and tuples
# https://aprendeconalf.es/docencia/python/ejercicios/listas-tuplas/


"""Exercise 1
Write a program keep  the topics of a class math, physic, chemistry, history and literature in a list and shoe them"""


topics = ["math", "physic", "chemistry", "history", "literature"]
print(topics)

"""Exercise 2
keep the topics like the first one, but print I study <topic> where it the variable that has the subjects"""

subjects = ["math", "physic", "chemistry", "history", "literature"]
for subject in subjects:
  print(f"I study: {subject}")
  
"""Exercise 3
Write a program that keep the same subjects, ask the user the note he/she take in each subject and show In<subject> you have taken <grade>"""

while True: 
  subjects = ["math", "physic", "chemistry", "history", "literature"]
  for subject in subjects:
    grades = int(input(f"How is your grade in {subject}: "))
    print(f"I took{grades} in {subject}")
  break


