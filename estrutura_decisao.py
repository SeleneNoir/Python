a = 10
b = 20

if (a > b):
    maior = a
else:
    maior = b

print(f'O maior número é: {maior}')

#Implementar uma solução que verifique se um número é par ou ímpar
numero = 46

if(numero%2 == 0):
    situacao = 'O número é par';
else: 
    situacao = 'O número é ímpar';

print(situacao);   

#Média

media = 8.5

if(media >= 7.0):
    situacao = 'Aprovado!'
elif(media >= 5.0):
    situacao = 'Em recuperaçao'
else: 
    situacao = 'Reprovado'

print(f"O estudante está: {situacao}")

#Exercício desconto
preco_unitario = 10;
DESCONTO10 = 0.1;
DESCONTO20 = 0.2;

quantidade = eval(input('Digite a quantidade desejada: '));

if(quantidade <= 10):
    valor_final = preco_unitario * quantidade;
elif (quantidade <= 20):
    valor_final = preco_unitario * quantidade * (1-DESCONTO10)
else:
    valor_final = preco_unitario * quantidade * (1-DESCONTO20)

print(f"O valor final da compra é: {valor_final}")

#For

lista = [10,2,5,7,6,3]
n = len(lista)
soma = 0
for i in range(n): #for num in lista:
    if(lista[i]%2 == 0):
        soma = soma + lista[i]
print(f"O somatório dos elemetos pares da lista é {soma}")