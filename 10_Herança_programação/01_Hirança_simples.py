class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.número_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")


class Motocicleta(Veiculo):
  pass

 
class Carro(Veiculo):
  pass


class Caminhao(Veiculo):
   def esta_carregado(self):
      print("Não estar carregado")


moto = Motocicleta("preta", "abc-1234", 2)
moto.ligar_motor()

carro = Carro("branco", "xde-0098", 4)
carro.ligar_motor()

caminhao = Caminhao("roxo","gfd-8712", 8)
caminhao.ligar_motor()
caminhao.esta_carregado()