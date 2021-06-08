def coordenadas_menor(matriz, menor):
    coordenada_menor = []
    for i_linha in range(len(matriz)):
        for i_coluna in range(len(matriz[i_linha])):
            if (matriz[i_linha][i_coluna] == menor and
                    len(coordenada_menor) == 0):
                coordenada_menor.append((i_linha, i_coluna))
    return coordenada_menor


def coordenadas_maior(matriz, maior):
    coordenada_maior = []
    for i_linha in range(len(matriz)):
        for i_coluna in range(len(matriz[i_linha])):
            if (matriz[i_linha][i_coluna] == maior and
                    len(coordenada_maior) == 0):
                coordenada_maior.append((i_linha, i_coluna))
    return coordenada_maior


def elementos_maior(matriz):
    maior = matriz[0][0]
    for vetor in matriz:
        for elemento in vetor:
            if elemento > maior:
                maior = elemento
    return maior


def elementos_menor(matriz):
    menor = matriz[0][0]
    for vetor in matriz:
        for elemento in vetor:
            if elemento < menor:
                menor = elemento
    return menor


def leitura_matriz(ordem):
    matriz = []
    for linha in range(ordem):
        vetor = []
        for coluna in range(ordem):
            numero = int(input(''))
            vetor.append(numero)
        matriz.append(vetor)
    return matriz


def main():
    # Leitura:
    ordem_matriz = int(input(''))
    minha_matriz = leitura_matriz(ordem_matriz)
    # Processamento:
    maior_elemento = elementos_maior(minha_matriz)
    menor_elemento = elementos_menor(minha_matriz)
    coordenada_maior = coordenadas_maior(minha_matriz, maior_elemento)
    coordenada_menor = coordenadas_menor(minha_matriz, menor_elemento)
    # Saída:
    for i in coordenada_maior:
        print(i)
    for i in coordenada_menor:
        print(i)


if __name__ == '__main__':
    main()
