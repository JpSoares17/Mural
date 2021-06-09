def maior(matriz):
    maior = matriz[0][0]
    for i_linhas in range(len(matriz)):
        for i_colunas in range(len(matriz[i_linhas])):
            if matriz[i_linhas][i_colunas] > maior:
                maior = matriz[i_linhas][i_colunas]
    return maior


def menor(matriz):
    menor = matriz[0][0]
    for i_linhas in range(len(matriz)):
        for i_colunas in range(len(matriz[i_linhas])):
            if matriz[i_linhas][i_colunas] < menor:
                menor = matriz[i_linhas][i_colunas]
    return menor


def media(matriz):
    soma = 0
    for i_linhas in range(len(matriz)):
        for i_colunas in range(len(matriz[i_linhas])):
            soma += matriz[i_linhas][i_colunas]
    return soma / (len(matriz) * len(matriz[0]))


def soma_ultima_linha(matriz, colunas):
    soma = 0
    for i_linhas in range(len(matriz)):
        for i_colunas in range(len(matriz[i_linhas])):
            if i_colunas == colunas-1:
                soma += matriz[i_linhas][i_colunas]
    return soma


def soma_primeira_linha(matriz):
    soma = 0
    for elementos in matriz[0]:
        soma += elementos
    return soma


def preencher_matriz(linhas, colunas):
    matriz = []
    for linha in range(linhas):
        vetor = []
        for coluna in range(colunas):
            elemento = int(input(''))
            vetor.append(elemento)
        matriz.append(vetor)
    return matriz


def main():
    # Leitura:
    dimensao_n = int(input(''))
    dimensao_m = int(input(''))
    minha_matriz = preencher_matriz(dimensao_n, dimensao_m)
    # Processamento:
    tupla_resposta = (
        soma_primeira_linha(minha_matriz), soma_ultima_linha(
            minha_matriz, dimensao_m),
        round(media(minha_matriz), 4), menor(minha_matriz),
        maior(minha_matriz))
    # Saída:
    print(tupla_resposta)


if __name__ == '__main__':
    main()
