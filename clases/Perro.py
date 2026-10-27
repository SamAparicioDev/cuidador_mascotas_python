from clases.Mascota import Mascota
from interfaces.Sonoro import Sonoro


class Perro(Mascota, Sonoro):

    @classmethod
    def hacer_sonido(self):
        print("El perro esta ladrando", "\n=========================" )

    def ladrar(self):
        print("Guau guau")

    def traer_pelotas(self):
        if self.energia <= 1:
            print("El perro esta cansado, no puede traer la pelota", "\n=========================")
        else:
            self.energia = self.energia - 2
            print(self.nombre, " trajo la pelota", "\n=========================")