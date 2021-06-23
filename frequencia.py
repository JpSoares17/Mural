from unicodedata import normalize


def tira_acento(texto):
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')


def contador(texto):
    letra = {}
    for letra_texto in texto:
        if ord('A') <= ord(letra_texto) <= ord('Z') and (
                letra_texto not in letra):
            letra[letra_texto] = 1
        elif ord('A') <= ord(letra_texto) <= ord('Z') and (
                letra_texto in letra):
            letra[letra_texto] += 1
        elif letra_texto in ",.()!?" and (
                letra_texto not in letra):
            pass
        elif letra_texto in ",.()!?" and (
                letra_texto in letra):
            pass
    return letra


def main():
    # Leitura:
    texto = input("").strip().upper()
    # Processador:
    texto_formatado = tira_acento(texto)
    frequencia = contador(texto_formatado)
    # Saída:
    print(frequencia)


if __name__ == "__main__":
    main()
