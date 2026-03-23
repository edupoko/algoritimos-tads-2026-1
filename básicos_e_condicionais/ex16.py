sexo = int(input("Digite 1 para masculino e 2 para feminino: "))
idade = int(input("Digite sua idade: "))

if sexo == 1 and idade >= 18:
    print("Pode alistar")
else:
    print("Nào cumpriu os requisitos")
