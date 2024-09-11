nome = input("Informe seu nome:")
idade = input("Informe sua idade")

# Utilizando o normal
print(nome, idade)

# Utilizando só  com o end.
print(nome, idade, end= "...\n")

#Utilizando o separador con o end.
print(nome, idade, sep= "#", end= "...\n")

# Utilizando só o  separador.
print(nome, idade, sep= "#")