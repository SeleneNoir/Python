#Bibliotecas em Python
#numpy

def entrada_dados():
    coeficiente = quantidade = eval(input('Coeficiente: '));
    return coeficiente; 

def calc_delta(a, b, c):
    delta = b * b - 4 * a * c;
    return delta; 

import numpy as np
def calcular_raizes(a, b, c, delta):
    if(delta < 0):
        resultado = 'A equação não possuí raiz nos números reais!';
    elif(delta == 0):
        x = -b / (2 * a);
        resultado = f'A equação possui apenas uma raiz: {x}'
    else: 
        x1 = (-b-np.sqrt(delta)) / (2 * a);
        x2 = (-b+np.sqrt(delta)) / (2* a);
        resultado = f'A equação possui as raizes: x1 = {x1} e x2 = {x2}';
    return resultado;

#f(x) = ax^2 + bx + c
a = entrada_dados();
b = entrada_dados();
c = entrada_dados();

delta = calc_delta(a, b, c);
resultado = calcular_raizes(a, b, c, delta);
print(resultado);


