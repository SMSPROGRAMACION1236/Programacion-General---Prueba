b# https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/

#Types of dates
# Exercise 1
# print a helloworld.



print("Hello World!")


# Exercise 2
# Create a variable it have a hello_world and then print it
hello_world = "Hello World!"
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
parts = euro(".")

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
amount_times_paid = float(input("Quantity to income "))
interest = float(input("¿faz of interest? "))
years = int(input("Years?"))
for i in range(years):
    amount_times_paid *= 1 + interest / 100
    print("Capital after " + str(i+1) + " years: " + str(round(amount_times_paid, 2)))
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
# TODO: I can do it better

"""
Exercise 4
Write a program ask the user about the winner numbers in the lottery and keep them in a list and show from little to big"""

lottery = []
for i in range(6):
  lottery.append(int(input("Type the winner numbers: ")))

lottery.sort()
print(str(lottery))

"""Exercise 5
Write a program that keep  the numbers in a list from 1 to 10 a print it in the opposite order with comas"""

not_together_numbers = []

for i in range(1,11):
  not_together_numbers.append(i)

not_together_numbers.sort(reverse=True)
print(not_together_numbers)

"""
Exercise 6
Write a program keep the subjects like math, physics, chemistry, history and literature in a list, ask to everyone about his note in each subject and delete the subjects that you passed. Show the subjects the user need to repeat"""

subjects = ["math", "physic", "chemistry", "history", "literature"]
grades = []
limit = 5
subjects_to_repeat = []


for subject in subjects:
  grade= input(f"What is your grade in {subject}: ")
  grades.append(grade)
for subject, grade in zip(subjects, grades):
  grade = int(grade)
  if grade < limit:
    subjects_to_repeat.append((subject))
print(f"The subjects like {subjects_to_repeat}, you  will to repeat because there are below of the limit {limit} of points")
"""
Exercise 7
Write a program keep the alphabet in a list, delete the letters
"""

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
filter_abc = [letter for index, letter in enumerate(abc, start=1) if index % 3 != 0]
print(filter_abc)

"""Exercise8
Write a program the user ask a word and show if it is a palindrome"""

palindrome = list(input("Enter a word"))
reversed_palindrome = palindrome[::-1]

if palindrome == reversed_palindrome:
  print("Yes")
else:
  print("No")

"""Exercise 9
Write a program ask a word y show it in the scream the number of times that has each vocal"""
#My solution

word = input("Enter a word: ").lower()

letters =  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

a = word.count(letters[0])
e = word.count(letters[4])
i = word.count(letters[8])
o = word.count(letters[15])
u = word.count(letters[21])

print(f"The letter a with {a} repetitions, letter e with {e} repetitions, letter i with {i} repetitions, letter p with {o} repetitions and letter u with {u} repetitions")
#The best solution

word = input("Type a word: ")
vocals = ['a', 'e', 'i', 'o', 'u']
for vocal in vocals:
    times = 0
    for letter in word:
        if letter == vocal:
            times += 1
    print("The vocal " + vocal + " is " + str(times) + " times")


"""Exercise 10
write a program keep the following prices 50, 75, 46, 22, 80, 65, 8 and show them the biggest and the smaller price"""

prices = [50, 75, 46, 22, 80, 65, 8]
prices.sort()
print(f"The lowest value is: {prices[0]}")
prices.sort(reverse= True)
print(f"The biggest value is: {prices[0]}")


"""Exercise 11
Write a program that keep the vectors (1,2,3) y (-1,0,2) in two lists and soft out the Scalar product"""
#Mine
vector1 = (1,2,3)
vector2 = (-1,0,2)
scalar_product = vector1[0]*vector2[0] + vector1[1]*vector2[1]+ vector1[2]* vector2[2]
print(scalar_product)

#not mine
a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(a)):
    product += a[i]*b[i]
print("the products  of the vectors" + str(a) + " y " + str(b) + " es " + str(product))


"""Exercise 12
Write a program that times two matrices, """
import numpy as np

first_matrix = np.array([[1,2,3],
                [4,5,6]])
second_matrix = np.array([[-1, 0],
                [0,1],
                [1,1]])
result = np.dot(first_matrix, second_matrix)
result = first_matrix @ second_matrix
print(result)


"""Exercise 13
Write a program ask the sample of numbers, separated by comas, keep in some lists and show  its mean and standard deviation."""
result = 0
sample = []
for i in range(5):
  sample.append(int(input("Enter: ")))
for i in sample:
  result+= i
print(result)

mean = result / (len(sample))
print("The mean is ", mean)


deviation = 0

for i in  (list(sample)):
  deviation += (i-mean) ** 2

standard = deviation /  len(sample)
print(standard**0.5)


### Dictionaries
# https://aprendeconalf.es/docencia/python/ejercicios/diccionarios/

"""Exercise 1
Write a program that keep {'Euro':'€', 'Dollar':'$', 'Yen':'¥'} in a dictionary ask the user for a badge and show his symbol  or say that that badge is not there"""

money = str(input("Enter: "))
badge = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
if money.title() in badge.keys():
  print(badge[money.title()])
else:
  print("It's not here")

"""Exercise 2
Write a program asking the user's name age address and phone number and them shoe them in a print"""

name = input("Your name: ")
age = input("Enter the age: ")
address = input("Your address: ")
phone_number = input("Your phone number: ")

personal_information = {"name": name, "age": age, "address": address, "phone number": phone_number}

print(f"{personal_information['name']} is {personal_information['age']} years old and live in {personal_information['address']} and the phone number is {personal_information['phone number']}")

"""Exercise 3
Write a program that keep the prices of fruit, ask to the user for a fruit and its kilos , and show the price of the numbers of kilos of fruit, if the fruit isn't there, show a message"""


fruits = {"Orange":0.70, "Banana":1.35, "Pear":0.85, "Apple":"0.80"}

fruit = input("What fruit would you like: ").title()
kilo = float(input("Enter the kilos of fruit: "))

if fruit.title() in fruits.keys():
  print(f"yes we have{fruit} and it'll cost {fruits[fruit] * kilo} € per kilo.")
else:
  print("we don't have it")
"""Exercise 4
Write a program that ask a date in the format dd/mm/aaaa  and show the data date but dd of <month> of aaaa, where <month> is the name of the month"""

month = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}

date = (input("Enter a data in dd/m/aaaa: " ))
date = date.split("/")
print(date[0], 'of', month[int(date[1])], 'of', date[2])

"""Exercise 5
write a program that keep the credits of the subjects {"Math":6,"Physics":4,"Chemistry":5} and show each one, <subject> has <credits> credits, where <subject> is each subject and <credits> the number of credits and last sum all of them"""

subjects = {"Math":6,"Physics":4,"Chemistry":5}


for k, l in subjects.items():
  print(f"{k} has: {l}")

"""Exercise 6
Write a program, with an empty dictionary and fill  with information about a person like name, sex, age, phone, email, etc, Each time the we add a new data we need to print it"""
name =""
age = ""
sex = ""
phone_number =""
mail = ""
identify = {"name":name, "age":age, "sex": sex, "phone_number":phone_number, "mail": mail}

while True:

  question = input("Add information(name/age/sex/phone_number/mail): ").lower()
  if question  == "name":
    identify["name"]= input("Type your name: ")
    print(identify["name"])
  elif  question == "age":
    identify["age"]= input("Type your age: ")
    print(identify["age"])
  elif   question=="sex":
    identify["sex"]= input("Type your sex: ")
    print(identify["sex"])
  elif question=="phone_number":
    identify["phone_number"]= input("Type your phone number: ")
    print(identify["phone_number"])
  elif question== "mail":
    identify["mail"]= input("Type your mail: ")
    print(identify["mail"])
  else:
    break
print(identify.items())
## The good resolution
person = {}
continuing = True
while continuing:
    clave = input('¿What class of data do you want to? ')
    valor = input(clave + ': ')
    person[clave] = valor
    print(person)
    continuing = input('¿Do you like to add more information (Yes/Not)? ') == "Yes"

"""Exercise 7
Write a program, using a dictionary as a bag, the program need to ask the article and its price and add it  to the dictionary, until decide to end to buying, and the the we print the totally list with the total cost"""

bag = {}
pricing = 0
following = True
while following:
  article = input("Type the name of the article: ")
  price = (input(article +  " How much does it cost?:"))
  bag[article] = price
  pricing += int(price)
  following =  input('¿Do you like to add more articles (Yes/Not)? ') == "Yes"
print("Buying List")
for article, price  in bag.items():
  print(article,"\t", price)
print("total",pricing)

"""Exercise 8
Write a program creating a dictionary of translator spanish-english, the user must type the words in spanish and english separated by : and each par of <word>:<translate> separated by comas, the program must create the dictionary with the words and the translations, late it must ask a phase in spanish and it'll use the dictionary to translate it, if the word isn't in the dictionary stop"""

dictionary = {}
word_for_dict = input("Enter a word: ")

for i in word_for_dict(","):
  key, value = i.split(":")
  # print(key,value)
  dictionary[key]=value
# print(dictionary)

phase = input("Enter a phase: ")

for i in phase.split():
  if i in dictionary:
    print(dictionary[i],end=" ")
  else:
    print(i, end=" ")
"""Exercise 9
Write a program that management the slope bills of paid of a company, the bills will keep in a dictionary where the key of each bill will be the number of the bill and the value of the cost of the bill, the program must ask to the user if he wants to add a new bill, pay a existing one or to end it, if he wish to add a new one, ask for the number of the bill and its cost and it'll add to the dictionary, if he likes to pay it ask about the number of the bill, and it'll delate, later of ach operation the program must show by scream the amount had until this moment and the slope amount of the paying"""

bills = {1:100,2:500,3:200}
print(bills.keys())
amount_times_paid = 0
amount_paid = 0
dont_pay_amount = 0
bills = {1:100,2:500,3:200}
print(bills.keys())
amount_times_paid = 0
amount_paid = 0
dont_pay_amount = 0
while True:
  question = str(input("What would you like do to(add/pay): ")).lower()
  if question == "add":
    bill_key = int(input("Enter the value of the bill: "))
    bill_value = int(input(f"The vale from {bill_key} is: "))
    if bill_key in bills.keys():
      print("It's exit, or would you like to pay: ")
    else:
      bills[bill_key] = bill_value
      print(bills)
  elif question =="pay":
    bill_key = int(input("Enter the value of the bill: "))
    value = bills.pop(bill_key)
    print(bills)
    amount_times_paid += 1
    amount_paid += value
    amount_of_bills = len(bills)
    print(amount_times_paid)
    print(amount_paid)
    print(amount_of_bills)
    print("f")
    ## From here problems
    dont_pay_amount = 0
    for i in bills:
      dont_pay_amount +=  bills.get(i,0)
      print(f"hello{dont_pay_amount}")
  else:
    break
"""Exercise 10
write a program that let to management the database of clients in a company, the clients will be keep in a dictionary, and their keys will be their NIF and the value will be another dictionary with the data of client(name, address, phone number, mail, preferential where preferential will be true if it is a preferential client ) the program must ask to the user for one option of the menu: 1. Add client 2. Delete Client. 3. Show client, 4. List of clients, 5. list of preferential clients, 6. Finish
Where
1. Ask for the customer's data, create a dictionary with the data and add it to the database.
2. Ask for the client's NIF and delete their data from the database.
3. Ask for the client's NIF and show their data.
4. Show a list of all clients in the database with their NIF and name.
5. Show the list of preferred customers from the database with their NIF and name.
6. Finish the program. """
clients = {}
option = ""
while option !='6':
  if option =="1":
    nif = input("Enter your nif: ")
    name =  str(input(f"Please enter your name: "))
    address = str(input("Type your address: "))
    phone_number =  int(input("Enter your phone number: "))
    mail = str(input("Enter your mail: "))
    preferential =  str(input("Are you a prefer(yes/no): ")).lower()
    client = {"name": name, "address":address, "phone_number":phone_number,"mail":mail,"preferential":preferential =="yes"}
    clients[nif] = client
  elif option == "2":
    nif = input("Enter your nif: ")
    if nif in clients:
      del clients[nif]
      print("Deleted!")
    else:
      print("Not found.")
  elif  option == '3':
    nif = input("Enter your nif: ")
    if nif in clients:
      for key, value in clients[nif].items():
        print(f"{key}: {value}")
    else:
      print("NIF not found.")
  elif option == "4":
    for key, value in clients.items():
      print(key, value['name'])
  elif  option == "5":
    for key, value in clients.items():
      if value['preferential']:
          print(key, value['name'])
  option = str(input("Enter the option(1/2/3/4/5/6): "))




##https://aprendeconalf.es/docencia/python/ejercicios/funciones/

"""Exercise 1
Write a function that say Hello Friend"""

def say_hello():
  print("Hello Friend")
say_hello()

"""Exercise 2
Write a function that pass it a name and print hello <name>"""

def say_hello(name):
  print(f"Hello: {name}")
name = input("Enter your name")
say_hello(name)

"""Exercise 3
Write a function that take a positive number and return its factorial"""


def calculate_vectorial(n):
  result = 1
  if n == 0 or n == 1:
    return result
  else:
    for i in range(1, n +1):
      result = result * i
    return result
n  = int(input("Enter a positive number: "))
while n  < 0:
  n  = int(input("Enter "))
"""Exercise 4
Write a function that calculate the total of the bill after applied IVA, the function must receive the amount without IVA and the IVA to apply and return the total of the bill, if we don't give the IVA, we need to put 21% in default"""

def calculate_bill(amount_without_iva, iva):
  if iva == 0:
    iva = 0.21 # 21%
    bill = iva * amount_without_iva
    total_bill = bill + amount_without_iva
    return round(total_bill)
  else:
    iva  = (iva/100) * amount_without_iva
    total_bill = (iva) + amount_without_iva
    return round(total_bill)
iva = int(input("Enter the IVA: "))
amount_without_iva = int(input("Enter the amount: "))
print(f"You'll pay: {calculate_bill(amount_without_iva, iva)}")

"""Exercise 5
Write a function that calculate the area of a circle and another to calculate the volume of a cylinder using the first function"""

import math
def calculate_circle_area(radius):
  area = math.pi * (radius ** 2)
  return round(area)

def calculate_cylinder_area(high, radius):
    base_area = calculate_circle_area(radius)
    volume = base_area * high
    return volume
radium = int(input("Enter the radium: "))
hight = int(input("Enter the hight: "))

print(f"The area of the circle is: {calculate_circle_area(radium)} and the volume of the cylinder is: {calculate_cylinder_area(radium, hight)}")

"""Exercise 6
Write a function that show numbers in a list and return the medium"""
numbers =[]

def medium(numbers):
  adding = 0
  dimension  = int(input("Enter the dimension of the list: "))
  for l in range(dimension):
    numbers.append(int(input("Type the winner numbers: ")))
  for i in numbers:
    adding += i
  result = adding  / len(numbers)
  return result
print(medium(numbers))

"""Exercise7
Write a function that receive some numbers in a list and return another list with its squares. """

sample =[1, 4, 6]
final_sample = []
def calculate_squares_sample(sample):
  for n in sample:
    final_sample.append(n **2)
  return final_sample
print(calculate_squares_sample(sample))

"""Exercise  8
Write a function that takes a sample of numbers in a list and returns a dictionary with their mean, variance, and standard deviation."""

numbers = []
adding = 0
dimension  = int(input("Enter the dimension of the list: "))
for l in range(dimension):
  numbers.append(int(input("Type the winner numbers: ")))

def operations(numbers):
  adding = 0
  for i in numbers:
    adding += i
  mean = adding  / len(numbers)
  return  mean
#Another thing

def variance_total(numbers, variance = 0):
  # variance = 0
  mean =  (operations(numbers))
  for i in numbers:
    variance +=  (i - mean )**2
  variance_final = variance / (len(numbers) -1)
  return variance_final
def standard_deviation(numbers):
  square = variance_total(numbers)
  deviation = square ** 0.5
  return deviation
print(f"The mean is: {operations(numbers)}")
print(f"The variance is: {variance_total(numbers)}")
print(f"The standard deviation is: {standard_deviation(numbers)}")

"""Exercise
9 Write a program that calculate the MCD and MCM."""

def MCD(a, b):
  while b:
    a, b = b, a % b
  return a

def MCM(a, b):
  return a * b // MCD(a, b )

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print(f"The MCD is: {MCD(a, b)}")
print(f"The MCM is: {MCM(a, b)}")

"""Exercise 10
Write  a program that become a decimal number to bin number and the opposite"""

def decimal_to_bin(number:int):
  binary = bin(number)
  return binary

def bin_to_decimal(number_bin:bin):
  decimal = int(number_bin, 2)
  return decimal

number = int(input("Enter a number: "))
number_bin = str(input("Enter a number: "))

print(f"From Decimal to Binary is: {decimal_to_bin(number)}")
print(f"From Binary to Decimal is: {bin_to_decimal(number_bin)}")

"""Exercise 11
Write a program that receive a string and return a dictionary with each word that have, and its frequency. Write another function that receive the dictionary done with the last function and return a tuple with the most used word and its frequency"""

def pre_dict(words):
  exclamation = {}
  for i in words.split():
    exclamation[i] = exclamation.get(i, 0) +1
  return exclamation
words = input("Enter: ")
print(pre_dict(words))


def dict_to_tuple(words):
  dictionary = pre_dict(words)
  key_max = max(dictionary, key=lambda k:dictionary[k])
  value_max = dictionary[key_max]
  finally_tuple = (key_max, value_max)
  return finally_tuple
print(dict_to_tuple(words))


#https://aprendeconalf.es/docencia/python/ejercicios/programacion-funcional/

"""Exercise 1
Write a function that applies a discount to a price and another that applies VAT to a price. Write a third function that receives a dictionary with the prices and percentages of a shopping basket, and one of the previous functions, and uses the passed function to apply the discounts or VAT to the products in the basket and return the final price from the basket."""

# origin_price = int(input("Enter the price: "))
# percentage = int(input("Enter the percentage: "))
# iva = int(input("Enter the iva: "))
# print(discount(origin_price, percentage))
# print(calculate_iva(origin_price, iva))

def discount(origin_price, percentage):
  return origin_price * (1 - percentage/100)

def calculate_iva(origin_price,iva):
  return origin_price * (1 + iva/100)

original_basket = {"apple":2.5, "milk":1.0,"bread":0.8}
def product_info(basket, function, option):
  final_price = 0
  for  price in basket.values():
    modify_price = function(price, option)
    final_price += modify_price
  return final_price


x = int(input("The percent of iva : " ))
y = int(input("The percent of discount: "))
price_with_discount = product_info(original_basket, discount ,y)
price_with_iva = product_info(original_basket, calculate_iva,x)
print(f"The total price with iva is: {round(price_with_iva)}")
print(f"The total price with discount is: {round(price_with_discount)}")
"""Exercise 2
Write a function that simulates a scientific calculator that allows you to calculate the sine, cosine, tangent, exponential and natural logarithm. The function will ask the user for the value and the function to apply, and will display a table with the integers from 1 to the entered value and the result of applying the function to those integers."""
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
        print(f"The original number is{i} and the transformation is: {sin(i)}")
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

"""Exercise 3
Write a function that receives another function and a list, and returns another list with the result of applying the given function to each of the elements in the list.."""

def  multiply(num):
  return num * 2
numbers = [1,  5, 3]

def multyply_list(multiply, numbers):
  for i in numbers:
    print(multiply(i))
multyply_list(multiply, numbers)
"""Exercise 4
Write a function that takes another Boolean function and a list, and returns another list with the elements of the list that return True when the Boolean function is applied to them."""
numbers = [1, 2, 5, 6, 8, 9, 10, 122, 14, 53, 56, 42, 63, 76, 27, 7, 258]
numbers_after_boolean  = []
def bolean(i):
  if i %2 == 0:
    return True
  else:
    return False

def after_bolean(bolean):
  for i in numbers:
    if  bolean(i) == True:
      numbers_after_boolean.append(i)
  print(numbers_after_boolean)
after_bolean(bolean)



"""Exercise  5
Write a function that receives a phrase and returns a dictionary with the words it contains and their length.
"""


def function():
  my_dictionary = {}
  phase = str(input("Enter a phase: "))

  for i in phase.split():
    word = i
    lenght = len(i)
    my_dictionary[word] = lenght
  return my_dictionary

print(function())

"""Exercise 6
Escribir una función reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas."""
def grade(score):
    if score < 5:
        return 'SS'
    elif score < 7:
        return 'AP'
    elif score < 9:
        return 'NT'
    elif score < 10:
        return 'SB'
    else:
        return 'MH'

def apply_grade(scores):


    return list(map(grade, scores))

print(apply_grade([6.5, 5, 3.4, 8.2, 2.1, 9.7, 10]))


"""Exercise 7
Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas."""
"""clave = input('¿What class of data do you want to? ')
    valor = input(clave + ': ')
    person[clave] = valor
    print(person)"""
def grade(score):
    if score < 5:
        return 'SS'
    elif score < 7:
        return 'AP'
    elif score < 9:
        return 'NT'
    elif score < 10:
        return 'SB'
    else:
        return 'MH'



new_topics = {}
def notes():
  topics ={"Math": 12, "Chemistry":23}
  for i ,j in topics.items():
    new_topics[i.upper()] = grade(j)
  return new_topics
print(notes())


"""Exercise 8
Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas aprobadas.
"""

def grade(score):
    if score > 15 :
        return 'SS'
    elif score > 10 and score < 15:
        return 'AP'
    elif score > 5 and score < 10:
        return 'NT'
    elif score > 3 and score < 5:
        return 'SB'
    else:
        return 'MH'
scores = ["SS", "AP", "NT"]




new_topics = {}
def notes():
  topics ={"Math": 12, "Chemistry":16}
  for i ,j in topics.items():
    if grade(j) in scores:
      new_topics[i.upper()] = grade(j)
  return new_topics
print(notes())



"""Exercise 9
Escribir una función que calcule el módulo de un vector."""

def vector(x,y,z):
  return  (x**2 + y**2 + z**2) ** 0.5

def calcultate_vector():
  x = int(input("Enter a number: "))
  y = int(input("Enter a number: "))
  z = int(input("Enter a number: "))
  return vector(x, y, z)
print(calcultate_vector())
"""Exercise 10
Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:

[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]
Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con los inmuebles cuyo precio sea menor o igual que el dado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las siguiente fórmula en función de la zona:

Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5"""
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
    
      
      
  

"""Exercise 11
Escribir una función que reciba una muestra de números y devuelva los valores atípicos, es decir, los valores cuya puntuación típica sea mayor que 3 o menor que -3. Nota: La puntuación típica de un valor se obtiene restando la media y dividiendo por la desviación típica de la muestra.d
"""
def calculate_mean(numbers) :
  mean = 0
  for i in numbers:
    mean +=i
  return  (mean/len(numbers))

def variance_total(numbers):
  variance = 0
  mean = calculate_mean(numbers)
  for i in numbers:
    variance += (i-mean)**2
  return (variance /(len(numbers ))-1)


def desviation(numbers):
  return  round((variance_total(numbers))**0.5,2)


def atipic(numbers):
  atipic_list =[]
  for i in numbers:
    if((i - calculate_mean(numbers))/desviation(numbers)) >3 or((i - calculate_mean(numbers))/desviation(numbers)) < -3:
      atipic_list.append(i)
  return( atipic_list)
print(atipic([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000]))



# Ejercicios de Depuracion
#https://aprendeconalf.es/docencia/python/ejercicios/depuracion/

"""Exercise 1
Corregir los errores sintacticos del siguiente programa:
contraseña = input('Introduce la contraseña: ")
if contraseña in ['sesamo'):
  print('Pasa')
else
  print('No pasa')
  """
contraseña = input('Introduce la contraseña: ')
if contraseña in ['sesamo']:
  print('Pasa')
else:
  print('No pasa')


"""Exercise 2
Detectar y corregir los errores del siguiente programa que aplica iva a una factura
base = input('Introduce la base imponible de la factura: ')
print(aplica_iva(base, iva))

def aplica_iva(base, iva = 21):
    base = base * iva
    return base

"""
base = float(input('Introduce la base imponible de la factura: '))


def aplica_iva(base, iva):
    recept = (base) * (iva/100)
    return recept + base
print(aplica_iva(base, iva=21))

"""Exercise 3
Detectar y corregir los errores del siguiente programa que calcula el producto escalar de dos vectores:"""

u = [1, 2, 3]
v = [4, 5, 6]
def producto_escalar(u, v):
    for i in range(len(u)):
         u[i] *= v[i]
    return sum(u)
print(producto_escalar(u,v))
"""Exercise 4
Detectar y corregir los errores del siguiente programa que devuelve y elimina el teléfono de un listín telefónico a través del nombre del usuario:
listin = {'Juan':123456789, 'Pedro':987654321}

def elimina(listin, usuario):
    del listin[usuario]
    return listin[usuario]

print(elimina(listin, 'Pablo'))"""
listin = {'Juan':123456789, 'Pedro':987654321}

def elimina(listin, usuario):
    if usuario in listin:
      del listin[usuario]
    return listin

print(elimina(listin, 'Juan'))
"""Exercise 5
Detectar y corregir los errores del siguiente programa que multiplica dos matrices:
a = ((1, 2, 3),
    (3, 2, 1))
b = ((1, 2),
    (3, 4),
    (5, 6))

def producto(a, b):
    producto = []
    for i in range(len(b)):
        fila = []
        for j in range(len(a[0])):
            suma = 0
            for k in range(len(a[0]+1)):
                suma += a[i][k] * b[k+1][j]
            fila[j] = suma
        producto[i] = tuple(fila)
    return tuple(producto)

print(producto(a, b))

"""
a = ((1, 2, 3),
    (3, 2, 1))
b = ((1, 2),
    (3, 4),
    (5, 6))

def producto(a, b):
    producto = []
    for i in range(len(a)):
        fila = []
        for j in range(len(b[0])):
            suma = 0
            for k in range(len(a[0])):
                suma += a[i][k] * b[k][j]
            fila.append(suma)
        producto.append(tuple(fila))
    return tuple(producto)

print(producto(a, b))
