class Mascota:
    def __init__(self, nombre , edad):
        self.nombre = nombre
        self.edad = edad
        self.hambre = 5
        self.energia = 5

    def saludar(self):
        if self.edad == 1:
            print("Hola, soy ", self.nombre, "y tengo", self.edad, " año", "\n=========================")
        else:
            print("Hola, soy ", self.nombre, "y tengo" , self.edad,  " años" , "\n=========================" )

    def comer(self):
        if self.hambre == 0:
            print(self.nombre, " ya esta lleno, no quiere comer más", "\n=========================")

        else:
            self.hambre = self.hambre - 1
            print("Muchas gracias, acabas de darle de comer a tu muscota llamada " , self.nombre,"\n=========================")

    def jugar(self):
        if self.energia == 0:
            print("La mascota está demasiado agotada", "\n=========================")

        else:
            self.energia = self.energia - 1
            self.hambre = self.hambre + 1
            print(self.nombre, "  jugo", "\n=========================")

    def dormir(self):
        self.energia = 10
        print(self.nombre, " durmío", "\n=========================")

    def cumplir_anios(self):
        self.edad = self.edad + 1
        print("felicitaciones, " , self.nombre, " celebra otro año de vida", "\n=========================")

    def mostrar_estado(self):
        print("Nombre: ", self.nombre)
        print("Edad : ", self.edad)
        print("Energia: ", self.energia)
        print("Hambre: ", self.hambre)