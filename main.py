class Produto:
    def __init__(self,altura,largura,comprimento,peso):
        self.altura = altura
        self.largura = largura
        self.comprimento = comprimento
        self.peso = peso
        self.area = self.altura * self.largura
        self.volume = self.area * self.comprimento
    
    def get_info(self):
        print(f'Altura: {self.altura}m, Largura: {self.largura}m, Comprimento: {self.comprimento}m, Peso: {self.peso}kg, Area: {round(self.area,5)}m², Volume: {round(self.volume,5)}m³')

produtoA = Produto(0.4,0.2,0.4,11.5)
produtoA.get_info()