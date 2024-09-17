def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antercesor = numero - 1
    sucessor = numero + 1

    return antercesor, sucessor

def func_3():
    print("Olá mundo")
    return None
  


print(calcular_total([10, 20, 34])) # 64
print(retorna_antecessor_e_sucessor(10)) # (9, 11)
print(func_3()) # retorna Nome