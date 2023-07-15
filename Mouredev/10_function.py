### Funciones ###

def my_function():
    print("Esto es una función")

my_function()
my_function()
my_function()


def sum_two_values (first_value: int, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)  # Aqui les asignamos los valores
sum_two_values(23434, 2342) 
sum_two_values("23", "3")
sum_two_values(1.4, 5.2)

def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

sum_two_values_with_return(10, 5)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

my_result= sum_two_values(1.4, 5.2)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}") # f para formatear

print_name(surname="Santiago", name= "Sanabria")

def print_name_with_default (name, surname, alias="Sin alias"):  # Poner alias como prederminado
    print(f"{name} {surname} {alias}")

print_name_with_default("Santiago", "Sanabria")

print_name_with_default("Santiago", "Sanabria", "SMS")


def print_upper_texts(*texts):
    for text in texts:    # Ponerlo en mayuscula
      print(text.upper())


print_upper_texts("Hola", "Python", "Mourede")
print_upper_texts("Hola")