#Tipo int
print(1_000_000);
print(type(1_000_000));

#Tipo float
print(type(50.0)); #Não usar vírgula para separar os decimais;

x = 50.0;
y = 50,0;

print(x); 
print(y); #Nesse caso ocorre a crição de uma tupla;

x = 5/2
print(x);

quocienteInteiro = 21//2;
print(quocienteInteiro);

resto = 21%2;
print(resto);

#Tipo complex (x + yj);
r = complex(2,5);
print(r); #(2+5j) ->  r.conjugate() retorna o  conjugado do número complexo;

w = 2+5j;
type(w);

#Bool
b =  2 < 3;
print(b);

n = not(2 < 3);
print(n);

#Operadores matemáticos
# Divisão inteira	//
print(f"Divisão: ", 9/2);

# Resto na divisão inteira	%
print(f"Resto na divisão inteira: ", 9%2);

# Valor absoluto abs(parâmetro)
print(f"Valor absoluto: ", abs(-2.5));

# Exponenciação **
print(f"Exponenciação: ", 2**4);