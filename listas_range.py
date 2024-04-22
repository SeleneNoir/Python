#Listas do tipo range
#O Python cria sequências de números inteiros

lista_1 = range(3) #(0,1,2)
lista_2 = range(2, 7) #(2,3,4,5,6)
lista_3 = range(2, 9, 3) #(2,5,8)

nomes = ['Laura', 'Lis', 'Guilherme', 'Enzo', 'Arthur']
for nome in nomes:
    print(nome)

nome = input("Entre com seu nome: \n")
for letra in nome:
    print(letra)

#While
palavra = input('Entre com uma palavra: \n ')
while palavra != 'sair':
    palavra = input('Digite sair para encerrar o laço: \n')
print('Você digitou sair e agora está fora do laço')

while True:
    print('Você está no primeiro laço.')
    opcao1 = input('Deseja sair dele? Digite SIM para isso. \n')
    if opcao1 == 'SIM':
        break  # este break é do primeiro laço
    else:
        while True:
            print('Você está no segundo laço.')
            opcao2 = input('Deseja sair dele? Digite SIM para isso. \n')
            if opcao2 == 'SIM':
                break  # este break é do segundo laço
        print('Você saiu do segundo laço.')
print('Você saiu do primeiro laço')

for num in range(1, 11):
    if num == 5:
        continue
    else:
        print(num)
print('Laço encerrado')

#pass atua sobre a estrutura if, permitindo que ela seja escrita sem outras instruções a serem executadas caso a condição seja verdadeira
for num in range(1, 11):
    if num % 2 == 0:
        pass
    else:
        print(num)
print('Laço encerrado')