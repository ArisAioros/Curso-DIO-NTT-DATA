salario = 2000


def salario_bonus(bonus, lista):
    global salario

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux={lista_aux}")

    salario == bonus
    return salario


lista = [1] # A lista 1 é um objeto imuntavel para uma função:
salario_com_bonus = salario_bonus(500, lista) # 2500
print(salario_com_bonus)