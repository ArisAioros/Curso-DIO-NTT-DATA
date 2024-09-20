# Importante é se tem um asteristico ou dois asteristico de pois colocar qualque nome.
def exibir_poema(data_extenso, *args, **kwargs): # *args recebe os valores como uma dupla.
    # Já o **kwargas seguinifica o recebemento de um dicionário.
    texto = "\n".join(args) # "\n" siguinifica quebra de linha: 
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}" # \n\n siguinifica duas quebra de linha: 
    print(mensagem)


exibir_poema(
    "Sexta-feira 26 de agosto",
    "Zen do Python",
    "Bonito é melhor que feio.",
    "Explicito é melhor que implícito.",
    "Simples é melhor que complexo.",
    "Complexo é melhor que complicado.",
    "Plano é melhor que aninhado.",
    "Esparso é melhor que denso.",
    "A legibilidade conta.",
    autor= "Tin Peters",
    ano= 1999,
)