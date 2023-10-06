### String ###

my_string = "Mi String"
my_other_string ='Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + ""+ my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)
my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)


# Formatear un string


name, surmane, age = "Jose", "Gonzalez", 46

print("Mi nombre es {} {} y mi edad es {} ".format(name,surmane,age))
print("Mi nombre es %s %s y mi edad es %d "%(name,surmane,age))