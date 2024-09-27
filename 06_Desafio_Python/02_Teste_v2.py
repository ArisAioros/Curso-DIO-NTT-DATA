import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, nome):
        self.nome = nome

class Conta:
    def __init__(self, agencia, numero, cliente, saldo):
        self.agencia = agencia
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo

class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            conta = self.contas[self._index]
            return f"""\
            Agência:\t{conta.agencia}
            Número:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
        """
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1

# Example usage
clientes = [Cliente("Alice")]
clientes = [Cliente("Bob")]
contas = [Conta("1234", "56789", clientes[0], 1500.50), Conta("2345", "67890", clientes[1], 2500.75)]

iterador = ContasIterador(contas)
for info in iterador:
    print(info)