# Loops

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else: # es opcional 
    print("Mi condición es igual o mayor que 10")
print("La ejecución continúa...")

while my_condition < 20:
    print(my_condition)
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es 15, se detiene la ejecución")
        break


print("La ejecución continúa...")


# For

my_list = [35 ,24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)



my_string = "Jose"

for letras in my_string:
    print(letras)
    
    
my_dict = {
    "Nombre":"Jose",
    "Apellidos":"Gonzalez",
    "Edad": 46, 1:"python",
    "Lenguajes": {"Python, Swift, Kotlin"},
    1:1.80
}

for dicts in my_dict:
    print(dicts)
    if dicts == "Edad":
        break
else:
    print("El bucle para el diccionario ha finalizado") 



for dicts in my_dict:
    print(dicts)
    if dicts == "Edad":
        continue
else:
    print("El bucle para el diccionario ha finalizado") 