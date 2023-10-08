### Listas ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35 ,24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))

my_other_list = [1.77, "Jose", "gonzalez"]
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[-1])
print(my_other_list[1])
print(my_other_list[-3])
#print(my_other_list[3])  esto es un error estamos fuera de rango IndexError 
print(my_other_list.count("Jose")) # count nos dice las veces que se repite un valor, para contar utilizamos len()

height, name, surname = my_other_list
print(name)

print(my_list + my_other_list) # concatemos dos listas 

my_other_list.append("Jdev")
print(my_other_list)
my_other_list.insert(0, 46)
my_other_list.insert(1,"rojo")
print(my_other_list)
my_other_list.remove("rojo") #elimina por nombre
print(my_other_list)
print(my_list)
my_list.pop() # elimina el ultimo elemento, pero retorna el elemento eliminado
print(my_list)
print(my_list.pop(2))
print(my_list)
del my_list[2] # elimina sin más por indice
my_new_list = my_list.copy()
my_list.clear()# elimina todos los elementos de la lista 
my_other_list.insert(1, "Rojo")
print(my_list)
my_other_list[1] = "Azul"
print(my_new_list)
my_other_list.reverse()
print(my_other_list)
my_new_list.sort()
print(my_new_list)
print(my_new_list[1:3]) # vemos una sublista dentro de la lista, no la creamos solo la vemos 





