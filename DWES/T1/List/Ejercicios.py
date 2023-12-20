def beneficios(lista, list1, list2):

    listbenef = []
    for i in range(len(lista)):
        benef = list1[i] - list2[i]
        listbenef.append((lista[i], benef))
    return listbenef


if __name__ == '__main__':
    listaProd = ['silla', 'mesa', 'cama', 'sofá', 'butaca']
    listaFact = [55, 150, 250, 300, 200]
    listaCost = [40, 100, 150, 225, 140]
    print(f"{beneficios(listaProd, listaFact, listaCost)}")
