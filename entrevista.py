def contador():
    quantidades = {}
    for i in range(1000):
        ano_nascimento = int(input('').strip())
        if ano_nascimento in quantidades:
            quantidades[ano_nascimento] += 1
        elif ano_nascimento not in quantidades:
            quantidades[ano_nascimento] = 1
    return quantidades


def main():
    # Leitura:
    dicionario = contador()
    # Processamento:
    keys = sorted(dicionario.keys(), key=int)
    # Saída:
    for ano in keys:
        print(f"{ano}: {dicionario[ano]}")


if __name__ == "__main__":
    main()
