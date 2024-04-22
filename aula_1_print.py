x = 5 
print(x, type(x))

nome = "Aldous Huxley";
print (nome);
print('Valor da var nome = {}'.format(nome));

# Atribuição múltipla
a, b = 1, 2;
print('Antes da troca');
print(f"O valor das variáeis: a = {a}, b = {b}");
temp = a;
a = b;
b = temp;
print('Primeira troca');
print(f"O valor dasvariáveis: a = {a}, b = {b}");

#Segunda troca
a, b = b, a;
print('Segunda troca');
print(f"O valor dasvariáveis: a = {a}, b = {b}");

#Equivalencia
x = 10;
print(f"x={x}");
x+=2;
print(f"x={x}");
x-=2;
print(f"x={x}");

y = 10;
y*=2;
print(f"y={y}");
y/=2;
print(f"y={y}");
y%=2;
print(f"y={y}");

def multiplicador(numero):
        a = 2 # esta variável tem escopo local
        print(f"Dentro da função, a variável 'a' vale: {a}")
        return a * numero

a = 3 # esta variável tem escopo global
b = multiplicador(5)
print(f"Fora da função, a variável 'a' vale: {a}")

def multiplicador_2(numero):
        return b * numero

b = 3 # esta variável tem escopo global
c = multiplicador(5)
print(f"A variável b vale: {c}")

print('##############################');
def multiplicador(numero):
        global a # todas as referências à variável a são para a global
        a = 2      # a global será alterado
        print(f"Dentro da função,  variável  'a' vale: {a}")
        return a * numero


a = 7  # esta variável tem escopo global
b = multiplicador(5)
print(f"A variável b vale: {b}")
print(f"Fora da função, a variável 'a' vale: {a}")