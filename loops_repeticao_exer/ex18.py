num = int(input("Digite um num: "))
soma_pares = 0
soma_impares = 0
tot_pares = 0
tot_impares = 0

while num < 0:
    print("Número negativo, apenas positivos são válidos")

    num = int(input("Digite um num: "))

for i in range(num + 1):
    if i % 2 == 0:
        soma_pares += i
        tot_pares += 1
    else:
        soma_impares += i
        tot_impares += 1

print(f"A soma dos pares é igual a {soma_pares} e quantidade {tot_pares}")
print(f"A soma dos impares é igual a {soma_impares} e quantidade {tot_impares}")

