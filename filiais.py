def soma_total(matriz):
    somas_array = []
    for i_linha in range(len(matriz)):
        soma = 0
        for i_coluna in range(len(matriz[i_linha])):
            soma += matriz[i_linha][i_coluna]
        somas_array.append(soma)
    return somas_array


def soma_array(array):
    soma_por_ano = []
    for i_matriz in range(len(array)):
        somas_por_filial = []
        for i_linha in range(len(array[i_matriz])):
            soma = 0
            soma = sum(array[i_matriz][i_linha])
            somas_por_filial.append(soma)
        soma_por_ano.append(somas_por_filial)
    return soma_por_ano


def mes(i_coluna):
    meses = (
        'Janeiro', 'Fevereiro', 'Março',
        'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro',
        'Outubro', 'Novembro', 'Dezembro')
    return meses[i_coluna]


def filial(i_matriz):
    filiais = ('Filial 1', 'Filial 2', 'Filial 3')
    return filiais[i_matriz]


def leitura_array(dimensoes, linhas, colunas):
    array = []
    for dimensao in range(dimensoes):
        matriz = []
        for linha in range(linhas):
            vetor = []
            for coluna in range(colunas):
                faturamento = int(input(''))
                vetor.append(faturamento)
            matriz.append(vetor)
        array.append(matriz)
    return array


def main():
    # Leitura:
    faturamento = leitura_array(4, 3, 12)
    # Processamento:
    soma_faturamento = soma_array(faturamento)
    soma_por_ano = soma_total(soma_faturamento)
    # Saída:
    for i_matriz in range(len(faturamento)):
        for i_linha in range(len(faturamento[i_matriz])):
            for i_coluna in range(len(faturamento[i_matriz][i_linha])):
                print(f'{i_matriz+2014};{filial(i_linha)};', end='')
                print(f'{mes(i_coluna)};', end='')
                print(f'{faturamento[i_matriz][i_linha][i_coluna]}')
            print(f'TOTAL {i_matriz+2014} {filial(i_linha).upper()};', end='')
            print(soma_faturamento[i_matriz][i_linha])
        print(f'TOTAL {i_matriz+2014} TODAS FILIAIS;{soma_por_ano[i_matriz]}')
    print(f'TOTAL PERÍODO TODAS FILIAIS;{sum(soma_por_ano)}')


if __name__ == '__main__':
    main()
