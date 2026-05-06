soma = 0
contagem = 0

while contagem <= 10:
    salario = float(input("Digitte seu salário: "))
    contagem += 1
    soma += salario

print(f"A média salarial é igual: {soma / contagem}")