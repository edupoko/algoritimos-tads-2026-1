#EX1
contador = 0
total = 0
valor_alto = int(input("Digite o limite superior: "))
valor_baixo = int(input("Digite o limite inferior: "))

while valor_baixo >= valor_alto:
    print("Limite inferior menor ou igual a valor_alto")
    valor_baixo = int(input("Digite o limite inferior: "))

for i in range(valor_alto, valor_baixo, -3):
    contador += 1
    total += i
    print(f"Contagem regressiva: {i}")

print(f"\nMédia: {total / contador}")
    
#EX2

participantes = 0
livros_totais = 0
pref_fic = 0
pref_nofic = 0

while participantes <= 5:
    nome_livro = input("\nDigite seu nome: ")
    participantes += 1

    quant_livros = int(input("\nDigite quantos livros vc leu esse ano: "))
    livros_totais += quant_livros


    print("\nQual Gênero vc prefere Ficção ou Não Ficção")
    genero = input("Digite 1 para Ficção ou 2 para nâo Ficção: \n")

    match genero:
        case "1":
            pref_fic += 1
        case "2":
            pref_nofic += 1
        case _:
            print("\nEntrada inválida:")
            
print(f"Livros totais lidos pelo grupo: {livros_totais}")
print(f"Porcentagem de pessoas que preferem ficção: {(pref_fic * 100) / (participantes)}")
print(f"Quantos participantes preferem nâo ficção: {pref_nofic}")

#EX3

tentativas = 0
codigo = 2024

while tentativas <= 4:

    cod_user = int(input("Digite um código de 4 digitos: "))

    if cod_user == codigo:
        print("Cofre aberto")
        break
    else:
        tentativas += 1
        print(f"Código errado, total de tentativas: {tentativas}")
        if tentativas == 5:
            print("Cofre bloqueado")

    if cod_user > codigo:
        print("O código digitado é maior")
    else:
        print("O código digitado é menor")

#EX4

soma = 0
total_produtos = 0
maior_cinquenta = 0

while True:

    produto = float(input("Digite o preço do produto ou 0 para sair: "))

    if produto == 0:
        break
    elif produto > 50:
        maior_cinquenta += 1
        total_produtos += 1
        soma += produto
    else:
        total_produtos += 1
        soma += produto

print("Total items cadastrados: ", total_produtos)
print("Valor total da compra: ", soma)
print("Quantos custam mais que 50: ", maior_cinquenta)
print("Média total dos produtos:", soma / total_produtos)

#EX5

cont = 0
for i in range(5):
    cont += 1
    for j in range(1, cont):
        print(f'{j}', end=' ')
    print()




    
    


    


