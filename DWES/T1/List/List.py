list = ["a", 2, "hola", "58", 565, 8, 8, "MUNDO"]
# list[Desde:hacia]
print(list[:2])
print(list[::2])
print(list[4:])
print(list[4::])
print(list[1:5]) # Desde el 1 incluido hasta 5 sin incluir
print(list[1::5]) # El 1 incluido y 5
print(list[::])
print(list[::-1])

# Delete From List
# del list[index::indexLimit]

# Function Count works like with String
# list.count(value, start=0, end=list.length)

# Function index
# list list.index(value,start=list[0], end=list.length)
pos = list.index(8, 6)
print(pos)

# Function Remove
# list.remove(element)
# DONT USE -> list = list.remove(element)

# Function pop
# list.pop(pos=list.length)

# Function append
# list.append(element=list.length)

# Function insert
# list.insert(pos, element)
# pos, element -> required

# Function extend()
# list.extend(iterable)
# iterable -> list, diccionary, etc
# Function length -> len

for i,j in enumerate(list):
    print("Indice {}, letra {}".format(i,j))

# Function sort
# Alfanumerica, ASC
# DESC ->
# list.sort(reverse=True) == list.reverse()
lista1 = ["banana", "Kiwi", "cherry", "Orange"]
lista2 = ["banana", "Kiwi", "cherry", "Orange"]
lista1.sort()
lista2.sort(key=str.lower)
print(lista1)
print(lista2) # Correct

# Personalizar funcion


def function(n):
    key_value = abs(n - 50)
    print(f"Keyvalue de {n}: {key_value}")
    return key_value


lista_num = [50, 36, 1 , 58 , 156, 5]
lista_num.sort(key=function)
print(lista_num)

