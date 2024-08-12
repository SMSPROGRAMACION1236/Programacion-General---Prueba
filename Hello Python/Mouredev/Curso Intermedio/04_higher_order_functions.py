### Higher Order Functions ###

from functools import reduce

def sum_one(value):
    return value + 1  # Funcion dentro de una funcion
def sum_five(value):
    return value + 5

def sum_two_values_add_value(first_value, second_value,f_suma):
    return f_suma(first_value + second_value)

print(sum_two_values_add_value(5, 2, sum_one))
print(sum_two_values_add_value(5, 2, sum_five))



### Closures ###


def sum_ten(original_value):
    def add(value):  # Una funcion dentro de otra
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)
 
print(add_closure(5))  

print(sum_ten(5)(1))


### Built-in Higher Order Functions ###
numbers = [2, 5, 10, 21, 3, 30]
#Map  # Para interar valores
def multiply_two(number):
    return number * 2
print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# filter  # Para filtrar
def filter_greater_than_ten(number):
    if number > 10: # Filtrar valores mayores que 10
        return True
    return False
    
print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))


# Reduce
2, 5, 10, 21, 3, 30
def sum_two_values(first_value, second_value):
    print(first_value) # Suma valor a valor
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values, numbers))  