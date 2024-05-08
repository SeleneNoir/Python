#Script principal.py
from threading import Thread
from multiprocessing import Process

#Exemplo de thread e processo que executam a mesma função

def funcao_a(nome):
    print(nome)

def main():
    t = Thread(target=funcao_a, args=("Minha Thread",))
    t.start()

    p = Process(target=funcao_a, args=("Meu Processo",))
    p.start()

if __name__ == '__main__':
    main()
