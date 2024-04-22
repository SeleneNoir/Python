#Emprego de procedimentos e funções
def encontrar_minimo(lista):
    minimo = lista[0]
    for elem in lista:
        if(elem < minimo):
            mminimo = elem
    return minimo

lista_teste = [2, 10 ,3, 1, 9 , 5]
menor = encontrar_minimo(lista_teste);
print("O menor elemento da lista é: [{}]".format(menor))

#Função que retorne a soma dos elementos pares de uma lista
def ehPar(n):
    r = (n%2 == 0)
    return r

def soma_par(list):
    soma = 0
    for num in list:
        if(ehPar(num)):
            soma += num;
    return soma

lista = [10, 2, 5, 7, 6, 3];
soma = soma_par(lista)
print(f"O somatório dos elementos pares da lista é: {soma}");

#Calculo do fatorial de um número
#n! = n(n -1)

#Estratégia 1
def fatoral_iterativo(n):
    f = 1
    for i in range (1, n + 1):
        f = f * i
    return f

#Estratégia 2
def fatoral_recursivo(n):
    if((n == 0) or (n == 1)):
        return 1
    return n * fatoral_recursivo(n - 1)

numero = 5
print(f"O fatorial de {numero} é: {fatoral_iterativo(numero)}")
print(f"O fatorial de {numero} é: {fatoral_recursivo(numero)}")

#Determinar se um número é ou não primo
def eh_primo(n):
    if(n < 2):
        return False
    i = n//2
    while(i > 1):
        if(n%i == 0):
            return False
        i = i - 1;
    return True

def imprimir_resultado(numero, resultado):
        mensagem = f"O número {numero}. NÃO é primo"
        if(resultado):
            mensagem = f"O número {numero}. É primo"
        return mensagem

numero = 7;
resultado = eh_primo(numero);
msg = imprimir_resultado(numero, resultado);
print(msg);

#Exemplo chamada de função
escolha = input("Escolha uma opção de função: 1 ou 2\n")
if escolha == "1":
    def func1(x):
        return x + 1
    s = func1(10)

else:
    def func2(x):
        return x + 2
    s = func2(10)

print(s);

#Procedimentos
# São aqueles que não retornam valores.

# Funções
# São aquelas que retornam valores

def taximetro(distancia):
    def calculaMult():
        if distancia < 5:
            return 1.2
        else:
            return 1

    multiplicador = calculaMult()
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * km_rodado) * multiplicador
    return valor


dist = eval(input("Entre com a distancia a ser percorrida em km: \n"))
pagamento = taximetro(dist)
print(f'O valor a pagar é R$ {pagamento}')

#Docstrings

#Determina o n-ésimo termo da sequência de Fibonacci
#definir uma string que serve como documentação de funções definidas pelo desenvolvedor. Ao chamar o utilitário help() passando como parâmetro a função desejada, essa string é exibida
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

print(help(fibo))


