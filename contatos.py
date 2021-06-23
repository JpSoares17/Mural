def deletar_nome(agenda):
    nome = input("").strip()
    if nome in agenda:
        del agenda[nome]
    elif nome not in agenda:
        print(f"{nome} não está na agenda.")


def deletar_numero(agenda):
    nome = input("").strip()
    if nome in agenda:
        telefone = input("").strip()
        for i_telefone in range(len(agenda[nome])):
            if telefone == agenda[nome][i_telefone-1]:
                del agenda[nome][i_telefone-1]


def incluir(agenda):
    nome = input("").strip()
    if nome in agenda:
        telefone = input("").strip()
        agenda[nome].append(telefone)
    if nome not in agenda:
        telefone = input("").strip()
        agenda[nome] = [telefone]


def novo(agenda):
    nome = input("").strip()
    if nome not in agenda:
        telefone = input("").strip()
        agenda[nome] = [telefone]
    elif nome in agenda:
        print("Nome já existe na agenda.")


def main():
    # Processamento:
    agenda = {}
    running = True
    # Saída:
    while running:
        opcao = input("").strip()
        if opcao == "1":
            novo(agenda)
        elif opcao == "2":
            incluir(agenda)
        elif opcao == "3":
            deletar_numero(agenda)
        elif opcao == "4":
            deletar_nome(agenda)
        elif opcao == "5":
            for nome in agenda:
                posicao = 0
                print(f"Nome: {nome}")
                print("  Telefone(s):")
                for telefone in agenda[nome]:
                    posicao += 1
                    print(f"    {posicao}. {telefone}")
        elif opcao == "0":
            running = False


if __name__ == "__main__":
    main()
