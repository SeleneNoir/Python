#Script funcao_iterable.py
lista = [1, 2, 3, 4, 5]

def triplica_itens(iterable):
    lista_aux = []
    for item in iterable:
        lista_aux.append(item * 3);
    return lista_aux

def main():
    nova_lista = triplica_itens(lista);
    print(nova_lista);

if __name__ == "__main__":
    main();

#Script funcao_map.py
lista = [1, 2, 3, 4, 5]

def triplica(item):
    return item * 3

def main():
    nova_lista = map(triplica, lista)
    print(list(nova_lista));

if __name__ == "__main__":
    main();

#Script funcao_map_lambda.py
lista = [1, 2, 3, 4, 5]

nova_lista = map(lambda item: item * 3, lista) #Função lambda

def main():
    print(list(nova_lista));

if __name__ == "__main__":
    main();
