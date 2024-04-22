#Listas
#Podem ser criadas das seguinte maneiras
listaVazia = [];
listaSeparadaPorVirgula = ['a'], ['a','b','c'];
# listaCompreendida = [x for x in iterable]; -> Iterable pode ser uma sequência, um container que suporte iteração ou um objeto iterador. 
list();

#Tuplas
#Sequencias imutáveis
t = (); #Tupla vazia;
tupla = ('a', 'b', 'c');
tuple(); #tuple(iterable) #Construtor
#Novamente, iterable pode ser uma sequência, um container que suporte iteração ou um objeto iterador. Por exemplo, tuple('abc') retorna ('a', 'b', 'c') e tuple( [1, 2, 3] ) retorna (1, 2, 3). 

#Range
# sequência imutável de números e frequentemente é usado em loops de um número específico de vezes, como o for.
#Ele pode ser chamado de maneira simples, apenas com um argumento.
#Por exemplo, range(3) cria a sequência (0, 1, 2).
#Para que a sequência não comece em 0, podemos informar o início e o fim como parâmetros
#range(2, 7) cria a sequência (2, 3, 4, 5, 6).

#Operadores sequencias comuns
#True se x for um subconjunto de s
print('x' in 's');
print('s' in 's');

# False se x for um subconjunto de s
print("#############")
print('x' not in 's');
print('s' not in 's');

# Concatenação de s e t
print("#############");
print("Str" + "ing");

# Concatenação de n (3) cópias de s (ing)
print("#############");
print(3 * "ing"); # (n*s)

# Caractere de índice i em s
print("#############");
print('String'[3]);

# Comprimento de s -> len(s)
print("#############");
print(len("String"))

# Menor item de s
print("#############");
print(min('String'));

# Maior item de s
print("#############");
print(max('String'));
