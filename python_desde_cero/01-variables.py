# Variable

my_variable = "My string variable"   # Para definir una variable snake_case, no tiene palabra reservada.
print(my_variable)
my_int_variable = 5
print(my_int_variable)
my_bool_variable = True   # en los booleanos siempre en mayusculas True False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_variable, my_int_variable, my_bool_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)

print("Este es el valor de:", my_bool_variable)

# función de sistemas
#  'len()' cuenta los caracteres incluido los espacios

print(len(my_variable))


# Variables en  una sola linea. ¡No se suele usar!
name, surname, alias, age = "Jose", "Gonzalez", "Jdev", 46
print("Me llamo:",name, surname, ". Mi edad es:", age, ". y mi alias es:", alias)

# Inputs 
'''
first_name = input('What is your name: ')
age_input = input('How old are you? ')
print(first_name)
print(age_input)
'''

# Cambiamos el tipo Python es de tipado debil, por lo que puedes cambiar el tipo a lo que quieras. CUIDADO
name = 45
age = "Jose"

print(name)
print(age)


# Mañana mas y mejor 


