from clases.Mascota import Mascota
from interfaces.Terrestre import Terrestre
from interfaces.Sonoro import Sonoro


class Gato(Mascota, Sonoro, Terrestre):

    def saltar(self):
        print("El gatito dio un salto", "\n=========================")

    def hacer_sonido(self):
        print("El gatito que se llama" , self.nombre, " ronronea", "\n=========================")

    def maullar(self):
        print("Miau")

    def rasgunar_sofa(self):
        print(self.nombre, " rasguño el sofa", "\n=========================")