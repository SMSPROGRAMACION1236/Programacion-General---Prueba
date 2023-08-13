### Lambdas ###

# Es como una funcion con la peculariedad de ser anonimas  es decir sin nombre


sum_two_values = lambda first_value, second_value:print( first_value + second_value)  # No tiene nombre y se puede almacenar en una variable, para asi nombrarlo o usarlo mas adelante 

print(sum_two_values(2, 5))  # Asi lo imprimimos

multiply_values = lambda first_value, second_values: first_value * second_values - 3
print(multiply_values(2, 6543))
def sum_three_Values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_Values(2)(2, 5))

# siempre debemos retunar para asi imprimirlo
