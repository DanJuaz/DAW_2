if __name__ == '__main__':

    dicCartas = {
            chr(0x1f0a1): 1,
            chr(0x1f0a2): 2,
            chr(0x1f0a3): 3,
            chr(0x1f0a4): 4,
            chr(0x1f0a5): 5,
            chr(0x1f0a6): 6,
            chr(0x1f0a7): 7,
            chr(0x1f0a8): 8,
            chr(0x1f0a9): 9,
            chr(0x1f0aa): 10,
            chr(0x1f0ab): 11,
            chr(0x1f0ad): 12,
            chr(0x1f0ae): 13,
        }

    print(chr(0x1f0a1))
    listaCartas = list(dicCartas)
    print(listaCartas)
    # Vamos a escoger una carta, vemos su puntuación.
    # Para ello vamos a usar la función 'choice' del paquete 'random
    from random import choice

    cartaEscogida1 = choice(listaCartas)
    puntos = dicCartas[cartaEscogida1]

    # Escogemos ahora otra carta, y sumamos su puntuación a la anterior
    cartaEscogida2 = choice(listaCartas)
    puntos += dicCartas[cartaEscogida2]

    # Vamos a mostrar ahora las cartas escogidas y la puntuación correspondiente:
    print("Se han seleccionado:", cartaEscogida1, cartaEscogida2)
    print("La puntuación es:", puntos)