class Pessoa:
    def __init__(self, nome, endereco): #self é um parâmetro de auto-referenc
        self.set_nome(nome);
        self.set_endereco(endereco);

    def set_nome(self, nome):
        self.nome = nome;

    def set_endereco(self,endereco):
        self.endereco = endereco;

    def get_nome(self):
        return self.nome;

    def get_endereco(self):
        return self.endereco;


# Instancia da classe
pessoa_1 = Pessoa('Alicei', 'Rua: Alvarez Ramos, 191');
pessoa_2 = Pessoa('Pablo', 'Rua: Escobar, 192');

#Imprimir cada um dos objetos
print(f'Nome: {pessoa_1.get_nome()}, endereço: {pessoa_1.get_endereco()}');
print(f'Nome: {pessoa_2.get_nome()}, endereço: {pessoa_2.get_endereco()}')