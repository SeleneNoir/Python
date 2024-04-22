hw = 'Hello world';
print(hw);

num = 10;
print(num);

#Entrada de dados
nome = input("Digite seu nome: ");
print(nome);

numero = input("Digite um inteiro: ");
print(type(numero)); # str

# Função eval() -> recebe uma string, mas trata como um valor numérico;
s = '1 + 2';
type(s); # str
resultado = eval(s)
print(resultado)

numero = eval(input("Digite um valor numérico: "));
numero = numero + 2;
print(numero);

# Atividade IMC
peso_str = input("Digite o valor do peso: ");
altura_str = input("Digite o valor da altura: ");

peso = float(peso_str);
altura = float(altura_str);

imc = peso / altura ** 2;

print('Seu IMC é:', imc);