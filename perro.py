class Perro:
    def __init__(self, nombre,):
        self.nombre = nombre

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau guau!")

    def reaccionar(self, accion, persona):
        if accion == "comida":
            print(f"\n{persona.nombre} le dio comida a {self.nombre}. está feliz y mueve la cola!")
        elif accion == "juguete":
            print(f"\n{persona.nombre} le dio un juguete a {self.nombre}. salta de la emoción!")
        elif accion == "acariciar":
            print(f"\n{persona.nombre} acarició a {self.nombre}. se acurruca feliz!")
        else:
            print(f"\n{self.nombre} no entiende lo que intentas hacer...")


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

yo = Persona("Sergio")
mi_perro = Perro("Kobe")

print(f"Hola, soy {yo.nombre} y este es mi perro {mi_perro.nombre}.\n")

mi_perro.ladrar()

yo.interactuar_con_perro(mi_perro)

