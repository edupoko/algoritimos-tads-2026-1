num = int(input("Digite um número: "))
contador = 1
soma = 0

while contador <= num:
    soma += 1/contador
    contador += 1
print(f"{soma:.2f}")