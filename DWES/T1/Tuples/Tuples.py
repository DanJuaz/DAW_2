def tuples(*args):
    """Función que recibe una tupla de números y devuelve el producto de todos ellos"""
    primertuple = args
    result = 1
    for i in primertuple:
        result *= i
    return result


def valormedio(*args):
    """Función que recibe una tupla de tuplas de números y devuelve una tupla con el valor medio de cada tupla"""
    medias = [] 
    for i in args:
        acumulado = sum(i)
        media = acumulado / len(i)
        medias.append(media)
    return medias


if __name__ == '__main__':
    print(tuples(1, 2, 3, 4))
    producto1 = (2, 5, 6)
    producto2 = (1, 6, 8)
    producto3 = (89, 2, 56)
    print(valormedio(producto1, producto2, producto3))
