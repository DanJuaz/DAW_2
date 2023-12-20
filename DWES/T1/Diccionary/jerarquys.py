dict1 = dict([(1, "Julio"), ("Fulanito", 2)])

dict2 = {
    "Marca": "Mecedez",
    "Año": 2003,
    "Color": "Blanco"
}
direcciones = {"Iker": "Errenteria", "Xabi": "Lekunberri", "Issam": "Marruecos", "Julio": "Altza"}

'''
direcciones = {
    "Iker": "Errenteria",
    "Xabi": "Lekunberri",
    "Issam": "Marruecos"
}
'''

# Update( if not exits -> ADD)
direcciones["Messi"] = "Maiami"
direcciones["Julio"] = "Donostia"
if __name__ == '__main__':
    # GET function take the keyValue for search
    print(f"{dict1.get('2')}")
    print(f"{dict1.get('Fulanito')}")
    print(f"{direcciones}")
    for clave, valor in direcciones.items():
        print(f"Nombre: {clave}, Direccion {valor}")
    print(direcciones.keys())
    print(direcciones.values())
    # If Key exits
    print('Altza' in direcciones)
    # If Value exits
    print('Altza' in direcciones.values())
    print(dict2.clear())
    # dictionary.pop(keyname, defaultvalue = ValueError)
    # dictionary.update(items)
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 3, 'c': 4}
    d1.update(d2)
    print(d1)

