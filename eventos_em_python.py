#Eventos em Python
#Tratamento de exceções

#Verifica a exceção se a entrada é, de fato, um número
try:
    x = int(input('Digite um número: '));
except ValueError:
    print("Entre com um número válido.");

#Verificar se o número é válido, e caso inválido, insistir até que o usuário escreva um número que seja válido.
while True:
    try:
        y = int(input('Digite um número: '));
        break;  
    except ValueError:
        print("Entre com um número válido.");

#Tratamento de exceção de divisão por Zero
def dividir(x, y):
    try:
        resultado = x / y;
        print("A resposta é: ", resultado);
    except ZeroDivisionError:
        print('Divisão por zero!');


dividir(3, 0);
dividir(3, 2);