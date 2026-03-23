# sistema de bilheres metrô

print("Bilhetes \n" \
"Bilhete unitário ................................1,30 \n" \
"Bilhete duplo ...................................2,60 \n" \
"Bilhete de 10 viagens ......................... 12,00 ")

valor = float(input("Digite o dinheiro a ser gasto: "))


if valor >= 1.30:
    bil_uni = valor / 1.30
    bil_uni_troco = valor % 1.30
    print(f"Com {valor} seriam possíveis comprar: {bil_uni:.0f} bilhetes únicos e de troca seria {bil_uni_troco:.2f}")
else:
    print("Não há como comprar nenhum bilhte")

if valor >= 2.30:
    bil_duplo = valor / 2.60
    bil_duplo_troco = valor % 2.60
    print(f"Com {valor} seriam possíveis comprar: {bil_duplo:.0f} bilhetes únicos e de troca seria {bil_duplo_troco:.2f}")

if valor >= 12.00:
    bil_10 = valor / 12.00
    bil_10_troco = valor % 12.00
    print(f"Com {valor} seriam possíveis comprar: {bil_10:.0f} bilhetes únicos e de troca seria {bil_10_troco:.2f}")




