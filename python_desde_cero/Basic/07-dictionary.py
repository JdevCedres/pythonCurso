# Dictionaries

my_dict = dict()
my_other_dict = {}

my_other_dict = {"nombre":"Jose", "Apellidos":"Gonzalez", "Edad": 46, 1:"python"}
print(my_other_dict)

my_dict = {
    "Nombre":"Jose",
    "Apellidos":"Gonzalez",
    "Edad": 46, 1:"python",
    "Lenguajes": {"Python, Swift, Kotlin"},
    1:1.80
}
print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])
my_dict["Nombre"] = "Pedro"
my_dict[1]
my_dict["Calle"] = "Calle Jose"
print(my_dict)
del my_dict["Calle"] # Borrar calle solo
print(my_dict)

print("Pedro" in my_dict) # aqui busca en la clave. No en el valo
print("Nombre" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.fromkeys(("nombre",1))) # se crea un diccionario pero sin valores


print(type(my_dict))
print(type(my_other_dict))