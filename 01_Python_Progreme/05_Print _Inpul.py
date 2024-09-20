nome = input("Informe seu nome:")
idade = input("Informe sua idade")

# Utilizando, normal.
print(nome, idade)

# Utilizando só com o finalizador \n.
print(nome, idade, end= "...\n")

# Utilizando o separador '#' com o finalizador \n.
print(nome, idade, sep= "#", end= "...\n")

# Utilizando apenas o separador.
print(nome, idade, sep= "#")