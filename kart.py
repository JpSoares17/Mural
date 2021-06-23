def leitura_tempos():
    dados = {}
    for corredor in range(6):
        nome = input("").strip()
        tempos = []
        for time in range(10):
            tempo = float(input("").strip())
            tempos.append(tempo)
        soma = round(sum(tempos), 1)
        dados[soma] = (nome, min(tempos))
    return dados


def main():
    # Leitura:
    corredores = leitura_tempos()
    # Processamento:
    ordem = sorted(corredores)
    posicao = 0
    # Saída:
    print("-------|----------------------|---------------|---------------",
          end="")
    print("|---------------")
    print(" Ordem |   Nome do Corredor   |  Tempo Total  |  Tempo Mé", end="")
    print("dio  | Melhor Volta  ")
    print("-------|----------------------|---------------|---------------",
          end="")
    print("|---------------")
    for tempo in ordem:
        posicao += 1
        media = round(tempo/10, 1)
        print(f"{posicao:^7}|{corredores[tempo][0]:^22}|", end="")
        print(f"{tempo:^15}|{media:^15}|{corredores[tempo][1]:^15}")
    print("-------|----------------------|---------------|---------------",
          end="")
    print("|---------------")


if __name__ == "__main__":
    main()
