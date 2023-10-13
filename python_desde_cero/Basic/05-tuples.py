# Tuples

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (46, 1.80, "Jose", "Gonzalez", "Jose")
print(my_tuple)

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Jose"))
print(my_tuple.index("Gonzalez"))# nos dice el indice donde está

#my_tuple[1] = 1.90 
#print(my_tuple) daría error es inmutable, no se puede modificar elementos, borrar elementos

my_sum_tuple = my_tuple + my_other_tuple # esta sería un nueva tupla con la suma de las dos.

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Jdev"
my_tuple.insert(1, "azul")
print(my_tuple)

my_tuple = tuple(my_tuple)
print(type(my_tuple))

# Lo que hicimos es cambiar la tupla por list hice modificaciones y la volví a convertí en tupla 

del my_tuple # la elimina del todo, no borra el contendio, se carga la variable entera