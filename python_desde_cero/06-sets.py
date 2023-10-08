# Sets

my_set = set()
my_other_set = {}

my_other_set = {"Jose","Gonzalez", 46}

print(len(my_other_set))

my_other_set.add("Jdev")
#print(my_other_set[0]) # Error, no se accede igual que en las listas
print(my_other_set) # Los set no es una estrucctura ordenado.
my_other_set.add("Jdev")
print(my_other_set) # No acepta elementos repetidos.

print("Gonzalez" in my_other_set) #buscar

# remove se  puede hacer igual que la listas 
# clear se pude hacer también
# del también lo podemos hacer... del es del sistema no de los sets

my_new_set =my_set.union(my_other_set).union("pytho","kotlin")
print(my_new_set)

