#Vamos a crear una clase hija 'Perro' a partir de la clase padre 'Animal'
# Definimos una clase padre
class Animal:
    pass # la instrucción pass no hace nada, pero evitamos el error cuando no se permite código vacío.

# Creamos una clase hija que hereda de la padre
class Perro(Animal): # ponemos como parámetro la clase padre
    pass # la instrucción pass no hace nada, pero evitamos el error cuando no se permite código vacío.
# Con el método __subclasses__() podemos ver qué clases descienden de una en concreto (Animal en este caso)
print(Animal.__subclasses__())
# Con el método __bases__ podemos ver la clase padre de la clase Perro
print(Perro.__bases__)
# veamos el código
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    # Método genérico pero con implementación particular posterior
    def comunicar(self):
        # Método vacío
        pass

    # Método genérico pero con implementación particular posterior
    def mover(self):
        # Método vacío
        pass

    # Método genérico con la misma implementación
    def descripcion(self):
        print("Soy un Animal de subclase", type(self).__name__,f"y tengo {self.edad} años")
#Ahora creamos una clase Gato que hereda de animal
# de momento sólo hereda atributos y métodos de la clase Animal
class Gato(Animal):
    pass

miGato = Gato('mamífero',5)
miGato.descripcion()
# Ahora vamos a crear varios animales concretos y sobreescrbir algunos de los métodos definidos
# en la clase Animal, como 'comunicar' o 'mover', ya que cada animal se comporta de una manera distinta.
class Perro(Animal):
    def comunicar(self):
        print("Guau!")
    def mover(self):
        print("Camina con 4 patas")
    # nuevo método que no está en la clase padre
    def morder(self):
        print("morder!")

class Gato(Animal):
    def comunicar(self):
        print("Miau!")
    def mover(self):
        print("Camina sigilosamente con 4 patas")
# Vamos a crear ahora los objetos correspondientes a cada clase, y utilizarlos
miGato = Gato('mamífero', 8)
miPerro = Perro('mamífero', 12)

miGato.comunicar() # Miau!
miPerro.comunicar() # Guau!

miGato.descripcion()  # Soy un Animal de subclase Gato y tengo 8 años
miPerro.descripcion() # Soy un Animal de subclase Perro y tengo 12 años

miPerro.morder() # morder!
class Gato(Animal):
    def __init__(self, especie, edad, dueño):
        # Opción 1
        # self.especie = especie
        # self.edad = edad
        # self.dueño = dueño

        # Opción 2
        super().__init__(especie, edad)
        self.dueño = dueño
miGato = Gato('mamífero',6,'Pedro')
print(miGato.especie)
print(miGato.edad)
print(miGato.dueño)
# Para saberlo se usa el método '__mro__' -> Method Order Resolution
class Clase1:
    pass
class Clase2:
    pass
class Clase3(Clase1, Clase2):
    pass

print(Clase3.__mro__)
# Vemos que comienza la búsqueda en la propia clase, y va subiendo a las clases padre
# en el orden con el que se han colocado los argumentos padre en la creación de la clase hija.
# Vemos al final la clase 'object'. Todas las clases en Python heredan de una clase genérica object.