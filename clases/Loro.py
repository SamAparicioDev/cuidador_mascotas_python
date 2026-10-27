from Mascota import Mascota
from interfaces import Aereo
from interfaces.Sonoro import Sonoro


class Loro(Mascota, Sonoro, Aereo):

    def hacer_sonido(self):
        print("El lorito parlotea", "\n=========================")

    def volar(self):
        print("El lorito esta volando", "\n=========================")


    def repetir(self, palabra):
        print(palabra, "\n=========================")