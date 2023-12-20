# ^ Inicio de una cadena
# $ para el final de una cadena
# . cualquier caracter menos espacio
# * lo qu eprocede se repita de 0 a n veces
# + 1 a n veces
# ? 0 a 1 vez
# (n) repita exacetamente n veces
# {m, n} se repita m n veces
# [] lista alternativa
# [0-5][0-9] -> 00 hasta 59
# | -> or
# finall(patron, cadena, flags=0) return a list contains the coincidences
# serach(patron, cadena, flags=0) retrun object with the words founded and the positions between has been founded
# EXPRESIONES REGULARES
# Las expresiones regulares nos permiten describir un patrón de búsqueda de cadenas de caracteres.
# Opciones principales:
# ^ para el inicio de una cadena.
# $ para el final de una cadena.
# . para cualquier carácter (salvo el salto de línea).
# * para precisar que lo que precede se repite de 0 a n veces.
# + para precisar que lo que precede se repite de 1 a n veces.
# ? para precisar que lo que precede se repite de 0 a una vez.
# {n} para precisar que lo que precede se repite exactamente n veces.
# {m, n} para precisar que lo que precede se repite entre m y n veces.
# [ ] para indicar una lista de alternativas.
# - [amk] busca 'a', 'm', o 'k'
# - [0-5][0-9] buscará los números de dos dígitos de 00 a 59
# - Si el primer carácter del conjunto es '^', coincidirán todos los caracteres que no estén en el conjunto. Por ejemplo, [^54] coincidirá con cualquier carácter excepto '5' y '4'
# | para indicar un O lógico entre dos expresiones.
# () para indicar un grupo (puede tener otros significados en función del primer carácter, según la apertura del paréntesis).
# \b: cadena vacía al inicio o final de la palabra.
# \B: cadena vacía que no está al principio o al final de una palabra.
# \d: indica un dígito.
# \D: indica cualquier carácter excepto un dígito.
# \s: indica un espacio (espacio, tabulación…).
# \S: indica cualquier carácter excepto un espacio.
# \w: indica una letra, un dígito o un carácter de subrayado.
# \W: indica cualquier cosa salvo una letra, un dígito o un carácter de subrayado.
# Python tiene un paquete integrado llamado re, que puede usarse para trabajar con expresiones regulares.
# Función 'findall'
# Devuelve una lista que contiene todas las coincidencias.
# SIntaxis: findall(patrón, cadena, flags=0)
# Los 'flags' nos sirven para modificar el comportamiento de la función. Por ejemplo, si queremos realizar una búsqueda insensible a las mayúsculas y minúsculas, tendremos que usar 'flags=re.IGNORECASE'
# [ ]
# # Vamos a buscar las palabras que empiezan por b
# # En Python, una 'raw string' es una cadena que permite incluir barras invertidas (\) sin interpretarlas
# # como secuencias de escape.
# import re
# re.findall(r'\bb\w*', 'el balón de baloncesto pesa más que el Balón de fútbol')
# account_circle
# ['balón', 'baloncesto']
# [ ]
# # Ahora vamos a buscar independientemente de si la palabra empieza por b mayúscula o minúscula
# re.findall(r'\bb\w*', 'el balón de baloncesto pesa más que el Balón de fútbol',flags=re.IGNORECASE)
# ['balón', 'baloncesto', 'Balón']
# Función 'search'
# Busca la primera palabra donde el patrón de expresión regular produce una coincidencia y devuelve un objeto con la palabra encontrada y el rango de las posiciones de las letras de la palabra encontrada [pos_inicio, pos_final+1).
# Sintaxis: search(patrón, cadena, flags=0)
# # Ejemplos
# texto = "la Real Sociedad este año está jugando muy bien y está obteniendo muy buenos resultados."
# # patrón para buscar una palabra que empieza por mayúscula
# patron = r"\b[A-Z][a-z]*\b"
# resultado=re.search(patron, texto)
# print(resultado)
# print(resultado.group())
# print(resultado.span())
# account_circle
# <re.Match object; span=(3, 7), match='Real'>
# Real
# (3, 7)
# Función 'sub'
# Reemplaza las coincidencias con el texto de nuestra elección.
# Sintaxis: sub(patrón, reemp, cadena, count=0, flags=0)
# - count («recuento») es el número máximo de reemplazos, por defecto es cero, todas las ocurrencias serán reemplazadas.
