dia = input("Digite um dia da semana: ")

match dia.lower():
    case "segunda" | "terça" | "terca" | "quarta" | "quinta" | "sexta":
        print("Tem aula")
    case "sabádo" | "sabado" | "domingo":
        print("Não tem aula")
    case _:
        print("Informe uma aula")