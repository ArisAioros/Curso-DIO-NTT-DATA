# Argumento nomeado são passado com {chave e valor}. Argumento nomeado passado sequencial só com posição, são parametros posicionais:
# Agumento nomeado pode ser foçado com asteristico:
# Quando quer por posição usar uma barra /. (ou os dois barra e asteristico):

def criar_carro(modelo, ano, placa, /, marca, *, motor, combustrivel):
    print(modelo, ano, placa, marca, motor,combustrivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustrivel="Gasolina") # valido:

# criar_carro(modelo="Palio", ano= 1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido
