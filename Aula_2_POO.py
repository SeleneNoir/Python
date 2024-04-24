class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome;
        self.idade = idade;

    def imprimir(self):
        print(self.nome, " tem ", self.idade, " ano(s)");
    
    def getIdade(self):
        return self.idade; 

    def setIdade(self, idade):
        self.idade = idade;

p = Pessoa("Kyle", 18);
p.imprimir();