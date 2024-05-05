class Veiculo:

    def __init__(self, nome, velocidade_max, quilometro_litro):
        self.nome = nome
        self.velocidade_max = velocidade_max
        self.quilometro_litro = quilometro_litro

    def toStr(self):
        print(f'Nome = {self.nome}. Velocidade máxima = {self.velocidade_max}. KMs percorridos = {self.quilometro_litro}')

modelo_carro = Veiculo('Fusca', 180, 10);
modelo_carro.toStr();