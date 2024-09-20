# Importante é se tem um asteristico ou dois asteristico de pois colocar qualque nome.
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema(
    "Sexta-feira 26 de agosto",
    "Zen do Python",
    "Bonito é melhor que feio.",
    "Explicito é melhor que implícito.",
    autor= "Tin Peters",
    ano= 1999,
)