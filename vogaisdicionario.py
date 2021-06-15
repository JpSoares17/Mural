from unicodedata import normalize


def gerar_dicionario(string_sem_acento):
    vogais = {
        "A": 0,
        "E": 0,
        "I": 0,
        "O": 0,
        "U": 0}
    for letra in string_sem_acento:
        if letra in ["A", "E", "I", "O", "U"]:
            vogais[letra] += 1
    return vogais


def remocao_acento(string):
    return normalize("NFKD", string).encode("ascii", "ignore").decode("utf-8")


def main():
    # Leitura:
    texto = input('').strip().upper()
    # Processamento:
    texto_sem_acento = remocao_acento(texto)
    vezes_vogais = gerar_dicionario(texto_sem_acento)
    # Saída:
    for chaves in vezes_vogais:
        print(f'{chaves}: {vezes_vogais[chaves]}')


if __name__ == '__main__':
    main()
