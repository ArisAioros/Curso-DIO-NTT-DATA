nome = input("Informe seu nome:")
idade = input("Informe sua idade")

# Utilizando o normal.
print(nome, idade)

# Utilizando só com o fim.
print(nome, idade, end= "...\n")

# Utilizando o separador com o final.
print(nome, idade, sep= "#", end= "...\n")

# Utilizando apenas o separador.
print(nome, idade, sep= "#")