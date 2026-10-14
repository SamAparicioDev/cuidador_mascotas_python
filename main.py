
class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud

    def obtener_salud(self):
        return self.salud

    def imprimir(self):
        return f"Su nombre es: {self.nombre}  y tiene:  {self.salud}  de salud"



personajes = [
    Personaje("Baltazar", 40),
    Personaje("Merlin", 30),
    Personaje("Morgana", 20),]


for personaje in personajes:
    print(personaje.imprimir())









