def primos(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

def exibir_primos_somar(n):
    soma = 0
    tot = 0
    for i in range(2, n + 1):
        if primos(i):
            soma += i
            tot += 1
    print(f"A soma dos {tot} números primos desse intervalo foi igual a {soma}")

num = int(input("Digite um número: "))

exibir_primos_somar(num)