def aniversario_cidades(lista, mes, populacao):
    resultado = []
    for info_cidades in lista:
        if info_cidades[4]==mes and populacao<info_cidades[5]:
            mes_digitado = mes_escrito(mes)
            cidades_escolhidas = f'{info_cidades[2]}({info_cidades[0]}) tem {info_cidades[5]} habitantes e faz aniversário em {info_cidades[3]} de {mes_digitado}.'
            resultado.append(cidades_escolhidas)
    return resultado
def mes_escrito(mesM):
    if mesM==1:
        return 'janeiro'
    if mesM==2:
        return 'fevereiro'
    if mesM==3:
        return 'março'
    if mesM==4:
        return 'abril'
    if mesM==5:
        return 'maio'
    if mesM==6:
        return 'junho'
    if mesM==7:
        return 'julho'
    if mesM==8:
        return 'agosto'
    if mesM==9:
        return 'setembro'
    if mesM==10:
        return 'outubro'
    if mesM==11:
        return 'novembro'
    if mesM==12:
        return 'dezembro'

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
    mes, populacao_base = int(input('Que mês você deseja pesquisar?')), int(input('A partir de que população? '))

    #Processamento:
    cidades = carrega_cidades()
    mes_digitado = mes_escrito(mes)
    cidades_escolhidas = aniversario_cidades(cidades, mes, populacao_base)

    #Saída:
    print(f'CIDADES COM MAIS DE {populacao_base} HABITANTES E ANIVERSÁRIO EM {mes_digitado}:'.upper())
    for cidades_selecionadas in cidades_escolhidas:
        print(cidades_selecionadas)
if __name__ == '__main__':
    main()
