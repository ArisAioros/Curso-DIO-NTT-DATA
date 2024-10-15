class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto()
        self.quantidade = quantidade
        self.valor = valor

class Relatorio:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        # Verifica se o objeto passado é uma instância da classe Venda.
        if isinstance(venda, Venda):
            self.vendas.append(venda)
        else:
            print("Erro: Objeto inválido. É necessário uma instância da classe Venda.")

    def calcular_total_vendas(self):
        total = 0
        for venda in self.vendas:
            # Calcula o total de vendas:
            total += venda.quantidade * venda.valor
        return total


def main():
    relatorio = Relatorio()
    
    for i in range(3):
        produto = input()
        quantidade = int(input())
        valor = float(input())
        venda = Venda(produto, quantidade, valor)
        relatorio.adicionar_venda(venda)
    
    # Exibe o total de vendas:
    print("930.0:", relatorio.calcular_total_vendas())


if __name__ == "__main__":
    main()