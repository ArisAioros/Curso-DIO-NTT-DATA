def analise_vendas(vendas):
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas) if vendas else 0
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input("Digite as vendas mensais separadas por espaço: ")
    # Converte a entrada em uma lista de inteiros
    vendas = list(map(int, entrada.split()))
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))