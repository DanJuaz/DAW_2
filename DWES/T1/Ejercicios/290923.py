import re


def recursivo(n):
    """
    que utilice una función recursiva para calcular la suma de los enteros positivos de n+(n-2)+(n-4)... (hasta que
    n-x <= 0).
    """
    if n <= 0:
        return 0
    suma = n + recursivo(n - 2)
    return suma


def suma_lista(lista):
    """
    Función recursiva
    para calcular la suma de los elementos de una lista que tiene algunos elementos tipo lista.
    """
    total = 0

    for i in lista:
        if isinstance(i, list):
            total += suma_lista(i)
        else:
            total += i
    return total


def elevar(a=0, b=2):
    """
    Escribir un programa Python para calcular el valor de 'a' elevado a 'b'.
    Ayuda: '0' elevado a 'b' será siempre '0' ; 'a' elevado a '0' será siempre '1'
    """
    result = 1
    if a == 0:
        return 0
    elif b == 0:
        return 1
    else:
        for i in range(b):
            result = a * a
        return result


def polidromo(a):
    """
    Escribir una función de Python que verifique si una cadena pasada es un palíndromo o no.
    Nota: Un palíndromo es una palabra, frase o secuencia que se lee igual hacia atrás que hacia adelante, por ejemplo:
    ojo, radar.
    """
    a = a.lower()
    return a == a[::-1]


def mayus_yminus(a):
    """
    Escribir una función de Python que acepte una cadena como parámetro de entrada y cuente el número
    de letras mayúsculas y minúsculas.
    Ayuda: utilizar las funciones 'isupper()' - 'islower()'
    """
    cm = 0
    cmi = 0
    c = 0
    for i in a:
        if i.islower():
            cmi += 1
        elif i.isupper():
            cm += 1
        else:
            c += 1
    return cm, cmi, c


def listas(*args):
    """
    Número variable de parámetros (sin nombrar).
    Los parámetros pueden ser palabras o listas de 2/3 palabras. La función debe reconocer
    para cada parámetro si es una lista o no.
    Si es una lista, indicar el número de elementos de la lista; 7
    si es una palabra, indicar que el parámetro es una palabra.
    """
    for arg in args:
        if isinstance(arg, list):
            c = 0
            for i in arg:
                c += 1
            return f"La lista{arg} tiene {c} elemntos"
        elif isinstance(arg, str):
            return f"Es la palabra {arg}"
        else:
            return "No es ni una palabra ni una lista"


def convertir_fecha(fecha_entrada):
    """Escribir un programa Python para convertir una fecha de formato aaaa-mm-dd al formato dd-mm-aaaa."""

    patron = r'(\d{4})-(\d{2})-(\d{2})'
    fecha_salida = re.sub(patron, r'\3-\2-\1', fecha_entrada)
    return fecha_salida


if __name__ == '__main__':
    print(recursivo(4))
    print(f"Sumar lista {suma_lista([5, 2, 3])}")
    print(f"Potencia: {elevar(a=2)}")
    print(f"El polidorom {polidromo('oja')}")
    mayus, minus, especial = mayus_yminus('Hola me llamo Julio Daniel y tengo aos')
    print(f"Mayusculas: {mayus}, Miudsculas: {minus}, Especiales: {especial})")
    print(listas(['a', 'b', 'c']))
    print(convertir_fecha("2003-06-11"))
