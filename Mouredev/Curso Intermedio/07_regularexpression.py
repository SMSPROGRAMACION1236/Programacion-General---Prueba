### Regular Expression ###
# estas tratan de analizar cadenas de textos

import re

my_string  = "This is the lesson N° 7: \nLesson calls Expresiones Regulares"
my_other_str  = " This is not lesson N° 6: Manejo de Ficheros"


match =re.match("This is the lesson", my_string, re.I)  # Intenta encontrar un patron desde el principio
print(match)
start, end = match.span()
print(my_string[start:end])

match = print(re.match("This is not the lesson", my_other_str))
print(match)

if match != None:
    print(match)
    start,end = match.span()
    print(my_other_str[start:end]) # Another forms are : is no, != and not


# print(match.span()) # Count the quantities of the input in this case is 18 caracters 

# print(match.m)


## search
search =re.search("lesson", my_string, re.I)

print(search)  # find any character  anywhere if so span dont do it


## findall
findall = re.findall("lesson", my_string, re.I)
print(findall) #list repeat the word or character to know how many repeats are there


##split

print(re.split(":",my_string))

##sub

my_sub = re.sub("Expresiones", "expresiones", my_string)  #  to change something for examples from capital to little letters
print(my_sub)

print(re.sub("lesson","LESSON", my_string, re.I)) # jUST CHANGE THE INITIAL ONE 


print(re.sub("Expresiones Regulares", "lesson", my_string, re.I))
print(re.sub("lesson|Lesson", "LESSON", my_string, re.I)) # EL | toma dos valores o mas creo xd
print(re.sub("[L|l]esson", "LESSON", my_string, re.I)) # EL | toma dos valores o mas creo xd

#patterns


pattern= r"[Ll]esson"  # look something specify using reverse words or expressions of Python
 
print(re.findall(pattern, my_string))
pattern= r"[Ll]esson|Expresiones"
print(re.findall(pattern, my_string))


pattern = r"[a-z]"
print(re.findall(pattern, my_string))
pattern = r"[0-9]"
print(re.findall(pattern, my_string)) # Por que solo hay el numero 7

print(re.search(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))


pattern = r"[l]."  # Coincidencias con esta letra
print(re.findall(pattern, my_string))

email = "sanabrasanti1236@gmail.com"

pattern = r"[a-zA-Z0-9]"
print(re.findall(pattern, email))