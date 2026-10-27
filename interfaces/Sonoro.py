from abc import ABC, abstractclassmethod


class Sonoro(ABC):

    @abstractclassmethod
    def hacer_sonido(self):
        pass
