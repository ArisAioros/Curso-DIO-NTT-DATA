# O upper converte todos os caracteres em maiúsculo
nome = "gULherRE"

print(nome.upper())
print(nome.lower())
print(nome.title())

# O title converte todos os caracteres em minúsculo exeto a primeira letra que é maiúscula.
texto = "  Olá mundo!    "

print(texto + ".")
print(texto.strip() + ".") # remove os espaços vasil na direira e esquerda.
print(texto.rstrip() + ".") # remove o espaço vasil na esquerda.
print(texto.lstrip() + ".") # remove o espaço vasil na direita.

# O lower converte todos os caracteres em minúsculos
menu = "python"

# junções e centralização de string, úteis para criação de menu.
print("###" + menu + "###") 
print(menu.center(14)) # Centralizar os caracteres.
print(menu.center(14, "#"))
print("-".join(menu)) # Junta e pontua os caracteres
