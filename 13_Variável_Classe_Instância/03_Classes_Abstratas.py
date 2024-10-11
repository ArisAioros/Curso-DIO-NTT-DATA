from abc import ABC, abstractmethod

# Classes abstratas
class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
     pass

    @abstractmethod # Metodos abstratos
    def desligar(self):
        pass

   
    @property

    def marca(self):# obrigatoriedade
        pass
    

class ControleTV(ControleRemoto):
    def ligar(self):
       print("Ligando a TV...")
       print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!") 

    @property
    def marca(self):
        return "Fhilco"


class ControleArcondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligada!")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArcondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)