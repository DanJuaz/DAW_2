
def get_numinput() -> int | None:
    res = input("Introduce un numero entero:")
    try:
        res = int(res)

    except ValueError:
        print(f"Errro: Tiene que ser un numero entero")
    else:
        return res
    finally:
        print(f"EL valor introducido fue {res}")


def getvalue_list(index, lista = ["Julio", "Daniel", "Azurduy"]):
    try:
        palabra = lista[index]

    except IndexError:
        print("El valor esta fuera del rango de la lista")
    else:
        return palabra

if __name__ == '__main__':
    get_numinput()
    print(getvalue_list(1))
