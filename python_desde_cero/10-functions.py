# Funciones

def my_funtion():
    print("Esto es una función")

my_funtion()

# Función con parametros

def sum_values (first_number, second_number):
    print(first_number + second_number)

sum_values(5, 7)

#FUnción con parametros de salida

def sum_values_return (first_value, second_value):
    return first_value + second_value

result = sum_values_return(10, 5)
print(result)

def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="González", name= "José")

# función con parametros por defectos.

def print_name_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_default("Jose","Gonzalez", "Jdev")
print_name_default("Jose","Gonzalez")

# se imprime varios textos varios textos 

def print_texts(*texts):
    for text in texts:
        print(text.upper())


print_texts("Hola", "Jose es el mejor", "Se acabo")

