from adivinaNum import *


vidas = 5
minimo = int(input("Minimo valor del intervalo : "))
maximo = int(input("Maximo valor del intervalo : "))
numRandom = get_number(minimo, maximo)
print(f"------------------------ Comienza el JUEGO ------------------------")
print(f"Adivina el numero entre el {minimo} y {maximo}")
print(f"Tienes {vidas} intentos para adivinar el número secreto.")
print("------------------------------------------------------------")

for vida in range(vidas):
    # Mientra que vida se encuentre en el rango vidas entra
    res = get_numinput()
    if numRandom != res:
        vidas_restantes = vidas - vida
        if res > numRandom:
            print(f"El número misterioso es menor que {res}. Te quedan {vidas_restantes} intentos.")

        else:
            print(f"El número misterioso es mayor que {res}. Te quedan {vidas_restantes} intentos.")
    else:
        print("¡Felicidades, has acertado!")
        break

else:
    print(f"Lo siento, el número secreto era {numRandom}. ¡Mejor suerte la próxima vez!")