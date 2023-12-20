import random


def get_numinput() -> int | None:
    res = int(input("Introduce un numero entero:"))
    try:
        return res
    except ValueError:
        return print(f"El numero {res} tiene que ser un entero")


def get_number(minimo, maximo):
    try:
        while minimo >= maximo and maximo <= minimo:
            minimo = int(input("Ingresa el número mínimo nuevamente: "))
            maximo = int(input("Ingresa el número máximo nuevamente: "))
        return random.randint(minimo, maximo)
    except ValueError:
        return print(f"El numero {maximo} o {minimo} tiene que ser un entero")
