class clase:
    atributo = "Esto es un atributo"

    def metodo(self):  # 'self' es una variable que representa la instancia de la clase,
        # y debe estar siempre ahí, en todos los métodos de la clase.
        return "Esto es un método"


print(clase.atributo)  # Esto es un atributo
clase.metodo  # accedemos al método sin invocarlo, se devuelve una instancia al método
# Ahora creamos una instancia/objeto
objeto = clase()
# Y accedemos al contenido del objeto, definido en la clase
objeto.atributo

objeto.metodo
# Vemos que el hecho de acceder al método devuelve, simplemente un objeto, pero no invoca al método.
# Para realizar dicha llamada es necesario agregar los paréntesis y pasar los argumentos necesarios.
# El vínculo entre el primer argumento (self) del método definido en la clase y
# la instancia se realiza de manera natural/automática.
objeto.metodo()


# Es importante tener clara la interconexión entre una instancia y su clase.
# Si se modifican los elementos de la clase, entonces se modifican
# también los elementos de la instancia/objeto.
class otraClase:
    otroAtributo = "Esto es otro atributo"

    def otroMetodo(self):
        return "Esto es un otro método"


clase.atributo = otraClase.otroAtributo
clase.metodo = otraClase.otroMetodo
# recordemos que 'objeto' es una instancia de tipo class -> 'clase'
# El atributo de la clase es dinámico, cualquier cambio realizado sobre éste afectará a la instancia.
print(objeto.atributo)  # imprime el valor del atributo 'otroAtributo' de 'otraClase'
objeto.metodo()
# Cuando el atributo de una instancia/objeto se modifica y recibe otro valor diferente al de la clase,
# se 'desvincula' del atributo de la clase
objeto.atributo = 'modificamos el atributo del objeto, ahora será diferente al de la clase'
print("el atributo de la clase:", clase.atributo)
print("el atributo de la instancia/objeto:", objeto.atributo)
# Si hacemos lo siguiente, asignamos el valor del atributo de la clase al atributo del objeto,
# pero NO se vinculan de nuevo
objeto.atributo = clase.atributo  # 'Esto es otro atributo'
# Si modificamos ahora el atributo de la clase
clase.atributo = 'atributo de clase modificado'
print(objeto.atributo)  # devuelve el atributo de la clase anterior a la modificación previa.


# Podemos considerar que el atributo de la clase contiene el valor por defecto y
# el atributo de la instancia contiene el valor asociado de manera duradera al objeto.
# Por eso el 'print(objeto.atributo)' no devuelve el nuevo atributo de la clase.
# vamos a crear una clase 'Perro' con un par de atributos de instancia: el nombre y la raza.
class Perro:
    # El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza):  # 'self' es una variable que representa la instancia de la clase,
        # y debe estar siempre ahí

        print(f"Creando objeto/perro {nombre}, {raza}")

        # Atributos de instancia/objeto
        self.nombre = nombre
        self.raza = raza


# Ahora que hemos definido el método '__init__' con dos parámetros de entrada,
# podemos crear el objeto pasando el valor de los atributos.
miPerro = Perro("Bat", "Terrier")

# Para acceder a los atributos del objeto -> 'miPerro.atributo'
print(miPerro.nombre)
print(miPerro.raza)


class Perro:
    # Atributo de clase
    especie = 'mamífero'

    # El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza):
        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza


miPerro = Perro("Bat", "Terrier")
# Podemos acceder al atributo de clase a través de la clase o del objeto
print("A través de la clase:", Perro.especie)
print("A través del objeto:", miPerro.especie)


class Perro:
    # Atributo de clase
    especie = 'mamífero'

    # El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza):
        print(f"Creando perro de nombre {nombre}, y raza {raza}")

        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza

    def ladra(self):  # método para el ladrido
        print("Guau")

    def camina(self, pasos):  # método para caminar, meter los pasos.
        print(f"Caminando {pasos} pasos")
        # Vamos ahora a crear usar un objeto de clase 'Perro'
        miPerro = Perro("Sur", "Terrier")
        miPerro.ladra()  # el parámetro 'self' se pasa por defecto, no hay que ponerlo
        miPerro.camina(8)  # 8 pasos, el parámetro 'self' se pasa por defecto, no hay que ponerlo

        # Vamos a ver cómo se definen los tres tipos de métodos
        class Clase:
            def metodo(self):
                return 'Método normal de instancia', self

            @classmethod
            def metododeclase(cls):
                return 'Método de clase', cls

            @staticmethod
            def metodoestatico():
                return "Método estático"


class Clase:
    def metodo(self, arg1, arg2):
        print(arg1, arg2)
        return 'Método normal', self


# Ahora creamos el objeto de class 'Clase'
miObjeto = Clase()
# Y accedemos al método del objeto
miObjeto.metodo("Hola", "mundo!")


class Clase:
    @classmethod
    def metododeclase(cls):
        return 'Método de clase', cls


# Se pueden llamar desde la clase
Clase.metododeclase()
# También se pueden llamar desde el objeto
miObjeto = Clase()
miObjeto.metododeclase()


class Clase:
    @staticmethod
    def metodoestatico(n1, n2):
        return "Método estático de suma", n1 + n2


# se le puede llamar desde la clase o desde el objeto
miObjeto = Clase()
Clase.metodoestatico(2, 3)
