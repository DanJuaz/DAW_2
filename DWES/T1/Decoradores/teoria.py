# Veamos una función dentro de otra
def funcion_ext():
    print("Código de la función externa")
    def funcion_int():
        print("Código de la función interna")
    funcion_int() ## llamamos a la función interna desde la externa.

# Ahora llamamos a la función externa, que llamará a su vez a la función interna.
funcion_ext()

# Evidentemente, no podemos llamar a la función interna desde fuera
funcion_int()

# Vamos a hacer ahora que la función externa haga un 'return' de la función interna
def funcion_ext():
    print("Código de la función externa")
    def funcion_int():
        print("Código de la función interna")
    return funcion_int # sin paréntesis, devolvemos el código de la función, no el retorno de su ejecución.

# Ahora podemos asignar esta función a una variable, por ejemplo mi_func
mi_func = funcion_ext()
# Ahora ejecuto el código de 'mi_func', que es el mismo que el de 'funcion_int'
mi_func()

# Vamos a pasar ahora una función como argumento de otra función
def funcion_arg():
    return "Código de la función argumento"

def mi_funcion(funcion_argumento):
    # en esta función podemos ejecutar el código de la 'funcion_argumento'
    print("Código de mi función")
    print(funcion_argumento()) # ejecutamos el código de la 'funcion_argumento'
                               # y escribimos lo que nos devuelve.

#Ahora ejecutamos 'mi_funcion' y le pasamos como argumento 'funcion_arg'
mi_funcion(funcion_arg) # evidentemente el parámetro es 'funcion_arg', no 'funcion_arg()'