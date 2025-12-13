from typing import Any
from abc import ABC, abstractmethod

class Animal (ABC):
    def __init__ (self, nome: str):
        self.nome = nome 

    @abstractmethod
    def fazer_som(self):
        pass

    @abstractmethod
    def mover(self):
        pass

    def apresentar_nome (self):
        print (f"Eu sou um(a) {self.nome}")

class Gato (Animal):
    def __init__ (self, nome: str):
        super().__init__(nome)

    def fazer_som (self):
        print ("MIAUUU")
    
    def mover (self):
        print ("Gatinho andou e arranhou o sofá")

class Cachorro (Animal):
    def __init__ (self, nome:str):
        super().__init__(nome)
    
    def fazer_som (self):
        print ("AUAUAUUU")

    def mover (self):
        print ("O doguinho rolou no chão")

class Vaca (Animal):
    def __init__ (self, nome:str):
        super().__init__(nome)
    
    def fazer_som (self):
        print ("MUUUUUU")
    
    def mover (self):
        print ("Vaquinha saiu do lugar para ir comer grama")

class Leao (Animal):
    def __init__ (self, nome:str):
        super().__init__(nome)
    
    def fazer_som (self):
        print ("ROOOOOARR")
    
    def mover (self):
        print ("Lion subiu na pedra para rugir bem alto")

def apresentar (animal:Animal):
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()    
    print (f"Tipo: {type(animal).__name__}")
    print("-" * 10)

animais: list[Animal] = [Gato("Gatinho"), Cachorro("Doguinho"), Vaca("Vaquinha"), Leao("Lion") ]

for animal in animais:
    apresentar(animal)
