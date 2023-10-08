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
print(f"Mi nombre es {name} {surmane} y mi edad es {age}")

# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(d)
print(f) 

# División

language_slice = language[1:3]
print(language_slice)


# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones del sistema

print(language.capitalize()) # ponte la primera letra en mayusculas
print(language.upper()) # retorna en mayusculas todo los caracteres
print(language.count("t")) # cuenta caracteres
print(language.isnumeric()) # nos dice que es un número
print(language.lower()) # retorna en minusculas
print(language.isupper()) # nos dice si está todo en mayusculas
print(language.startswith("Py")) # preguntamos si empieza por en este caso por Py, nos dará true


















