conta_nomal = False
conta_universitaria = True
conta_especial = True

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_nomal:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")

elif conta_universitaria:

    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("saldo insuficiente!")

elif conta_especial:
    print("Canta especial selecionada!")

else:
    print("Sistema não reconhece seu tipo de conta, entre em contato com o seu gerente.")