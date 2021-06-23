def jogar():
    dado = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
        }
    while True:
        numero = int(input('').strip())
        if numero == 0:
            break
        dado[numero] += 1
    return dado


def main():
    # Leitura:
    resultados = jogar()
    # Saída:
    print(f"O dado foi lançado {sum(resultados.values())} vezes.")
    for face in resultados:
        print(f"A face {face} saiu {resultados[face]} vezes.")


if __name__ == "__main__":
    main()
