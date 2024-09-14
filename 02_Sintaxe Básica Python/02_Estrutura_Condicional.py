maior_idade = 18
idade_especial = 17

idade = int(input("Informe sua idade:"))

if idade >= maior_idade:
    print("Maior de idade, pode tirar a CNH.")

    if idade < maior_idade:
        print("Ainda não pode tirar a CNH.")


if idade >= maior_idade:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.")


if idade >= maior_idade:
    print("Maior de idade, pode tirar a CNH.")
elif idade == idade_especial:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")