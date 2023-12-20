def validar_arguemntos(func):
    """
    Escriba un programa Python que implemente un decorador para validar los argumentos de una función según una
    condición determinada. La función a decorar es calcular_cubo, que calcula el cubo de un parámetro x dado ( x3 ).
    El decorador será @validar_argumentos y debe comprobar si la 'x > 0'. En ese caso se llama a la función a
    decorar. Si no se cumple la condición, lanzar una excepción tipo 'ValueError'.
    """
    def comprobar(*args):
        if args[0] > 0:
            return func(*args)
        else:
            return ValueError("El arguemnto debe ser de mayor a 0")

    return comprobar


@validar_arguemntos
def calcular_cubo(x):
    return x ** 3


def convert_datatype(func):
    """Crear un decorador para convertir el valor de retorno de una función a un tipo de dato específico.
    El decorador tendrá un parámetro de entrada que será el tipo de dato al que se quiere convertir el valor de retorno
    de la función a decorar.
    En este caso hay dos funciones internas anidadas, ya que la externa recibe como
    parámetro el tipo de dato al que hay que convertir la salida de la función a decorar.
    La primera función interna será el decorador propiamente dicho que recibe
    como parámetro la función a decorar (y tendrá su función interna
    que tiene que devolver el resultado convertido al tipo de dato correspondiente). Hay que hacer dos funciones a
    decorar con el mismo decorador (aunque con distinto tipo de dato). Crear una función 'suma' que sume dos valores
    pasados como parámetros, con el parámetro 'int' para el decorador. Crear otra función que concatente dos
    palabras, con el parámetro 'str' para el decorador."""


if __name__ == '__main__':
    print(calcular_cubo(7))
