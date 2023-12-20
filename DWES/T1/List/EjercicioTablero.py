def funciolista():
    list1 = ["a", "b", "c", "d", "e", "f", "g", "h"]
    list2 = [1, 2, 3, 4, 5, 6, 7, 8]
    letra = input(f"Dime la posiicon albabetica{list1}: ")
    num = int(input(f"Dame la posicion numerica{list2}: "))

    if list2.count(num) == 1 and list1.count(letra) == 1:
        if num + list1.index(letra) % 2 == 0:
            print(f"La posicioon {letra} y {num} es NEGRA")
        else:
            print(f"La posicioon {letra} y {num} es BLANCA")
    else:
        print("TE CAGASTE")


def funciondiccionario():
    diccionario = dict([("a", 1), ("b", 2), ("c", 3), ("d", 4), ("e", 5), ("f", 6), ("g", 7), ("h", 8)])
    inp = input(f"Dime la posiicon del diccionario: {diccionario.keys()}: \n(pj:b2)")
    letra = inp[0]
    num = int(inp[1])
    num2 = diccionario[letra] + 1
    if letra in diccionario.keys() and num in diccionario.values():
        if (num + num2 % 2) == 0:
            print(f"La posicioon {letra} y {num} es NEGRA")
        else:
            print(f"La posicioon {letra} y {num} es BLANCA")

    else:
        print("TE CAGASTE")


if __name__ == '__main__':
    funciolista()
    funciondiccionario()
