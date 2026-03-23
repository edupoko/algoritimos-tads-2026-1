from datetime import date

data_atual = date.today()
ano_atual = data_atual.year
idade = int(input("Digite sua idade: "))

if idade >= 16:
    print("Apto a votar")
else:
    print("Ainda não pode votar")