# Quando desejamos que a saída siga determinado padrão – por exemplo, de hora ou de data – existem algumas possibilidades para usar a função print(). 
hora = 10
minutos = 26
segundos = 18

print(str(hora) + ':' + str(minutos) + ':' + str(segundos));

#Porém, existe outra possibilidade, usando o método format();
print('{}:{}:{}'.format(hora, minutos, segundos));
print(f'{hora}:{minutos}:{segundos}');

#Também é possível especificar a largura de campo para exibir um inteiro
print(f'{10:4}, {100:5}')

print('{:8.5}'.format(10/3)); #Define quantos valores aparecem após o ponto flutuante


#Impressão de sequencias
seq = [0, 1, 2]
print(seq);

str = 'Hello World';
print(str[0:4]);
print(str[2:8]);
print(str[: : -1]); #Lê da direita para a esquerda
print(str[8:2:-1]);
