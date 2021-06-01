def selecao_cidades(lista, num_populacao):
    resultado = []
    for info_cidades in lista:
        if info_cidades[5]>num_populacao:
            cidades_escolhidas = f'IBGE: {info_cidades[1]} - {info_cidades[2]}({info_cidades[0]}) - POPULAÇÃO: {info_cidades[5]}'
            resultado.append(cidades_escolhidas)
    return resultado
            
def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado

def main():
    #Leitura:
    populacao_base = int(input(''))

    #Processamento:
    cidades = carrega_cidades()
    cidades_escolhidas = selecao_cidades(cidades, populacao_base)

    #Saída:
    print(f'CIDADES COM MAIS DE {populacao_base} HABITANTES:')
    for cidades_selecionadas in cidades_escolhidas:
        print(cidades_selecionadas)
if __name__ == '__main__':
    main()
