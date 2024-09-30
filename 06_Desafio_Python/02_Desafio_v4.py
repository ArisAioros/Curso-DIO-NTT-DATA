def produto_mais_vendido(produtos):
    contagem = {}
    
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    max_produto = None
    max_count = 0
    
    for produto, count in contagem.items():# Encontre o produto com a maior 
        if count > max_count:
            contagem
            max_count = count
            max_produto = produto
    
    return max_produto

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input("Notebook, Mouse, Teclado, Mouse, Monitor, Mouse, Teclado:")
    # Converte a entrada em uma lista de strings, removendo espaços extras
    produtos = entrada.strip().split()
    
    return produtos

produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))