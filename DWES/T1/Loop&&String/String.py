# Function count
# String.count(value, start, end)
# value -> requiared, start,end -> optional
cadena = "Cadena m de texto haber cuanto aparece texto en este texto"
print(f"Se repite la palabra ´texto´: {cadena.count('texto')}")

# Function index
# String.index(value)
pos = cadena.index("m")

# Function replace
# String.replace(oldValue, value, count)
# oldValue, value -> required   count -> optional,many times to replace
cadenaReplace = cadena.replace('m', " de ejemplo", 1)
print(cadenaReplace)

# Import string
# function ASCII (.ascii_lowecase, ascii_digits.....)

# Function split
# String.split(separator, maxSplit)
#cadenaSplit = cadena.split(" ", 1)
cadenaSplit = cadena.split(" ")
print(cadenaSplit)

# Function join
# String.join(iterable)
# itirable -> requeired
# !!!
cadenaJoin1 = cadena.join(" ")
cadenaJoin = " ".join(cadenaSplit)
print(f"{cadenaJoin1}")
print(f"{cadenaJoin}")