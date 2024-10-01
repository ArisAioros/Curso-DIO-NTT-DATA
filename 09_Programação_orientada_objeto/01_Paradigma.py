class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    def buzinar(self):
            print("Plim plim...")
            
    def parar(self):
            print("Parando bicicleta...")
            print("Bicicleta parada!")

    def correr(self):
            print("Vrummmm...")
# Usando uma pratica que não é comum o uso do get_cor:
    #def get_cor(self):
     #   return self.cor
            

# bi = Bicicleta("vermelha", "caloi", 2022, # 600)
# bi.buzinar()
# bi.correr()
# bi.parar()
# print(bi.cor, bi.modelo, bi.ano, bi.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
b2.buzinar()# Bicicleta.buzinar(b2)
print(b2.cor)