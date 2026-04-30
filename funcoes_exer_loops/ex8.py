def pesquisa_renda():
    soma_s1f, cont1 = 0, 0
    soma_s2f, cont2 = 0, 0
    soma_s0f, cont0 = 0, 0

    for _ in range(3):
        nome = input("\nDigite seu nome: ")
        sal = float(input("Digite seu salário: "))
        filhos = int(input("Número de filhos: "))

        if filhos == 0:
            cont0 += 1
            soma_s0f += sal
        elif filhos == 1:
            cont1 += 1
            soma_s1f += sal
        elif filhos == 2:
            cont2 += 1
            soma_s2f += sal
            
    media0 = soma_s0f / cont0 if cont0 > 0 else 0
    media1 = soma_s1f / cont1 if cont1 > 0 else 0
    media2 = soma_s2f / cont2 if cont2 > 0 else 0
    
    total_pessoas = cont0 + cont1 + cont2
    media_geral = (soma_s0f + soma_s1f + soma_s2f) / total_pessoas if total_pessoas > 0 else 0

    print(f"\nO salário médio (2 filhos): {media2}")
    print(f"O salário médio (sem filhos): {media0}")
    print(f"O salário médio geral: {media_geral}")

    if media1 > media2:
        print("Média de 1 filho é maior.")
    else:
        print("Média de 2 filhos é maior (ou igual).")
        
pesquisa_renda()