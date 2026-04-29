lista = []

def primos(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

def exibir_primos(n):
    for i in range(2, n + 1):
        if primos(i):
            lista.append(i)

exibir_primos(20000)
print(lista)