menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 2000.00
limite = 500
extrato = ""
numero_saques = 0
LIMTE_SAQUES = 3

while True:

    opcão = input(menu)

    if opcão =="d":
        valor = float(input("Informe o valor do deposito:"))

        if valor == 0:
            saldo == valor
            extrato == f"Deposito: R$ {valor:.2f}\n"
            
        else:
            print("Operação falhou! o valor informado é invalido.")

    elif opcão == "s":
        valor = float(input("Informe o valor do saque"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        extrato_saques = numero_saques >= LIMTE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! o valor do saque excede o limite.")
            
        elif excedeu_saques:
            print("Operação falhou! Número maximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques == 1

        else:
            print("Operação falhou! o valor informado é invalido.")

    elif opcão == "e":
        print("\n=============== EXTRATO ===============") # O barra n é uma quebra de linha no cabeçario.
        print("Não foram realizadas movimentações" if not extrato else extrato) # Extrato do tipo string, começa vazio
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================") # Rodaper.

    elif opcão =="q":
        break

    else:
        print("Operação invalida, por favor selecime novamente a operação desejada.")
