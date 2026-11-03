from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def falar(self):
        pass

    @abstractmethod
    def mover(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return f"{self.nome}: Au au"

    def mover(self):
        return f"{self.nome} corre"

class Gato(Animal):
    def falar(self):
        return f"{self.nome}: Miau"

    def mover(self):
        return f"{self.nome} pula"

class Vaca(Animal):
    def falar(self):
        return f"{self.nome}: Muuu"

    def mover(self):
        return f"{self.nome} caminha"

class Voador:
    def voar(self, nome):
        return f"{nome} voa"

class Nadador:
    def nadar(self, nome):
        return f"{nome} nada"

class Pato(Animal, Voador, Nadador):
    def falar(self):
        return f"{self.nome}: Quack"

    def mover(self):
        return f"{self.nome} anda, {self.voar(self.nome)} e {self.nadar(self.nome)}"

class Jacare(Animal, Nadador):
    def falar(self):
        return f"{self.nome}: vá pra casa"

    def mover(self):
        return f"{self.nome} anda e {self.nadar(self.nome)}"

def fazer_som(animal: Animal):
    print(animal.falar())

def fazer_movimento(animal: Animal):
    print(animal.mover())

if __name__ == "__main__":
    rex = Cachorro("Rex")
    mimi = Gato("Mimi")
    richard = Gato("Richard")
    mimosa = Vaca("Mimosa")
    donald = Pato("Donald")
    ze_jacare = Jacare("Zé Jacaré")

    fazer_som(rex)
    fazer_movimento(rex)

    fazer_som(richard)

    fazer_som(mimi)
    fazer_movimento(mimi)

    fazer_som(mimosa)
    fazer_movimento(mimosa)

    fazer_som(donald)
    fazer_movimento(donald)

    fazer_som(ze_jacare)
    fazer_movimento(ze_jacare)