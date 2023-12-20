# Veamos un ejemplo:
def mi_decorador(funcion_argumento):
    def funcion_interna(): # función que 'envuelve' a la original a decorar
        print("Código antes de ejecutar la 'funcion_argumento' a decorar")
        funcion_argumento() # es la función a decorar
    return funcion_interna

def funcion_a_decorar():
    print("¡Necesito decoración!")

mi_decorador(funcion_a_decorar) # No se imprime nada, la función interna no es llamada desde 'mi_decorador'.
                                  # 'mi_decorador' devuelve el código de 'funcion_interna', pero no lo ejecuta.
                                  # Al ejecutarse el código de 'funcion_interna' se ejecutará el de 'funcion_argumento',
                                  # ya que 'funcion_interna' llama a 'funcion_argumento()'
# Vamos a recoger la 'funcion_interna' en una variable
funcion_decorada = mi_decorador(funcion_a_decorar)
# La 'funcion_decorada' recogida tiene la 'funcion_a_decorar' como 'funcion_argumento', por
# lo que cuando ejecutemos 'funcion_decorada' se ejecutará también 'funcion_a_decorar'
funcion_decorada()


# Una forma de hacer lo mismo en Python, sin tener que definir la variavle 'funcion_decorada', es la siguiente:
def mi_decorador2(funcion_argumento):
    def funcion_interna2():
        print("Código 2 antes de ejecutar la 'funcion_argumento' a decorar")
        funcion_argumento()

    return funcion_interna2


@mi_decorador2  # añadimos funcionalidad a 'funcion_a_decorar' sólo poniendo
# '@mi_decorador2' encima de la definición de 'funcion_a_decorar'
# El código añadido está en el decorador, que podemos añadir o no.
def funcion_a_decorar():
    print("¡Necesito decoración!")


funcion_a_decorar()

# Vamos a usar ahora un número variable de parámetros de entrada para el decorador.
def mi_decorador_p(funcion_argumento): # va a recibir 'funcion_argumento' con parámetros
    # print(f'argumentos antes de función interna: {args}')
    print("Se está ejecutando el decorador")
    def funcion_interna_p(*args, **kwargs):
        print(f"Código antes de ejecutar la 'funcion_argumento' a decorar, con argumentos {args}")
        funcion_argumento(*args, **kwargs)
    return funcion_interna_p

'''
Una opción es declarar la variable 'funcion_decorada' con la función que nos devuelve
mi_decorador_p (que es el código de 'funcion_interna_p', incluida su definición), y
luego ejecutar la función 'funcion_decorada'. Esta función puede ser llamada con un número variable
de parámetros, pero llama a su vez (con el mismo nº de argumentos) a la 'funcion_argumento' a decorar, 
que en nuestro caso tiene dos argumentos. Por tanto, si hacemos la llamada con un nº de argumentos
diferente a 2, nos dará error.

Otra  opción es usar un decorador.
'''
# OPCIÓN 2
#@mi_decorador_p
def funcion_a_decorar(nombre, edad):
    print(f"{nombre} tiene {edad} años")

#funcion_a_decorar("Pedro", 50) # se ejecuta esta función decorada -> se ejecuta la función decoradora y se devuelve
# su función interna, que se ejecuta con los mismos parámetros de entrada, y que a su vez llama a 'funcion_a_decorar'.
'''
Al hacer la llamada "funcion_a_decorar("Pedro", 50)", "funcion_a_decorar" es una función
decorada por 'mi_decorador_p', que llama a su función interna con estos mismos parámetros.
Si definiéramos 'def funcion_interna_p()' sin parámetros y ejecutásemos, el error sería:
# TypeError: funcion_interna_p() takes 0 positional arguments but 2 were given.
'''

# OPCIÓN 1
funcion_decorada = mi_decorador_p(funcion_a_decorar)
funcion_decorada("Pedro", 50)

funcion_a_decorar


# Ejemplo uso autorizado
def requiere_autorizacion(f):
    def funcion_decorada(*args, **kwargs):
        print(args)
        if not args[0]:
            print("Error. El usuario no está autorizado")
        else:
            f(*args, **kwargs)

    return funcion_decorada


@requiere_autorizacion
def entrar_al_sistema(autorizado):
    print("Hola, estás autorizado")


entrar_al_sistema(True)