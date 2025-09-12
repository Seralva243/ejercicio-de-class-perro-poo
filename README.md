# autor: Sergio alejandro vazquez pineda
# Primero creamos la clase del perro simplemente con un nombre, y le damosla opcion de ladrar
class Perro:
    def __init__(self, nombre,):
        self.nombre = nombre

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau guau!")

# ahora definimos cual sera la reaccion, y la accion que hace la persona, si la accion es de tal forma entonces pongo que yo hice tal accion y que kobe reacciono de tal manera
# y asi con cada accion o si no elige esa accion el perro no entiende lo que quiero hacer

    def reaccionar(self, accion, persona):
        if accion == "comida":
            print(f"\n{persona.nombre} le dio comida a {self.nombre}. está feliz y mueve la cola!")
        elif accion == "juguete":
            print(f"\n{persona.nombre} le dio un juguete a {self.nombre}. salta de la emoción!")
        elif accion == "acariciar":
            print(f"\n{persona.nombre} acarició a {self.nombre}. se acurruca feliz!")
        else:
            print(f"\n{self.nombre} no entiende lo que intentas hacer...")

# ahora creamos la clase de la persona que seria yo, definimos que la interaccion sera con el perro y le damos las opciones
# entonces si elegimos tal accion el perro reaccionara de tal forma acorde a la accion las cuales ya definimos anteriormente
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def interactuar_con_perro(self, perro):
        print(f"\n{perro.nombre} está triste. ¿Qué quieres hacer?")
        print("\n1. Dar comida")
        print("2. Dar juguete")
        print("3. Acariciar")

        opcion = int(input("\nElige una opción: "))
        if opcion == 1:
            perro.reaccionar("comida", self)
        elif opcion == 2:
            perro.reaccionar("juguete", self)
        elif opcion == 3:
            perro.reaccionar("acariciar", self)
        else:
            print("Opción no válida.")

# ahora pues definimos quien es quien, yo soy sergio y mi perro es kobe, nos presento, mi perro ladra y finalmente yo interactuo con kobe.
yo = Persona("Sergio")
mi_perro = Perro("Kobe")

print(f"Hola, soy {yo.nombre} y este es mi perro {mi_perro.nombre}.\n")

mi_perro.ladrar()


yo.interactuar_con_perro(mi_perro)

# Esta seria la salida 
Hola, soy Sergio y este es mi perro Kobe.

Kobe dice: ¡Guau guau!

Kobe está triste. ¿Qué quieres hacer?

1. Dar comida
2. Dar juguete
3. Acariciar

Elige una opción: 1

Sergio le dio comida a Kobe. está feliz y mueve la cola!
