idade = int(input("Digite sua idade: "))
peso = int(input("Digite seu peso: "))
resul = "Pode doar sangue" if idade >= 18 and peso >= 50 else "Não pode doar sangue"
print(resul)