def media_por_fabricante(tabela, linhas):
    medias = []
    for i in range(linhas):
        soma = 0
        for linha in tabela[i]:
            soma += linha
        media = round(soma/len(tabela[i]), 2)
        dados = (media, fabricante(i))
        medias.append(dados)
    return medias


def maior(lista):
    maior = lista[0][0]
    for dados in lista:
        if dados[0] > maior:
            maior = dados[0]
    for dados in lista:
        if dados[0] == maior:
            retorno = dados
    return retorno


def dados_coluna(tabela, colunas):
    soma_coluna = []
    for i in range(colunas):
        dados = [0, 0]
        for i_linha in range(len(tabela)):
            for i_coluna in range(len(tabela[i_linha])):
                if i_coluna == i:
                    dados[0] += tabela[i_linha][i_coluna]
                    dados[1] = i
        soma_coluna.append(dados)
    return soma_coluna


def fabricante(linha):
    fabricantes = ('Fiat', 'Ford', 'GM', 'Wolkswagen')
    return fabricantes[linha]


def maior_vendedor_ano(tabela, ano):
    maior = 0
    linha = 0
    for i_linha in range(len(tabela)):
        for i_coluna in range(len(tabela[i_linha])):
            if (i_coluna == (ano-2013)) and (
                    tabela[i_linha][i_coluna] > maior):
                maior = tabela[i_linha][i_coluna]
                linha = i_linha
    fabricante_selecionado = fabricante(linha)
    return fabricante_selecionado, maior


def leitura_tabela(linhas, colunas):
    matriz = []
    for linha in range(linhas):
        vetor = []
        for coluna in range(colunas):
            carro = int(input(''))
            vetor.append(carro)
        matriz.append(vetor)
    return matriz


def main():
    # Leitura:
    tabela = leitura_tabela(4, 6)
    ano_pesquisado = int(input(''))
    # Processamento:
    maior_vendedora, vendas_maior = maior_vendedor_ano(tabela, ano_pesquisado)
    dados_por_coluna = dados_coluna(tabela, 6)
    venda_maior_ano = maior(dados_por_coluna)
    media_fabricante = media_por_fabricante(tabela, 4)
    # Saída:
    print(f'A fabricante que mais vendeu em ', end='')
    print(ano_pesquisado, end=' ')
    print(f'foi a {maior_vendedora} com {vendas_maior} mil unidades.')
    print(f'O ano de maior volume geral de vendas foi ', end='')
    print(venda_maior_ano[1]+2013, end=' ')
    print(f'com {venda_maior_ano[0]} mil unidades.')
    print('A média anual de vendas de cada fabricante entre 2013 e 2018 foi:')
    for dados in media_fabricante:
        print(f'A {dados[1]} vendeu em média', end=' ')
        print(f'{dados[0]} unidades por ano.')


if __name__ == '__main__':
    main()
