def mes_escrito(mesM):
    if mesM==1:
        return 'JANEIRO'
    if mesM==2:
        return 'FEVEREIRO'
    if mesM==3:
        return 'MARÇO'
    if mesM==4:
        return 'ABRIL'
    if mesM==5:
        return 'MAIO'
    if mesM==6:
        return 'JUNHO'
    if mesM==7:
        return 'JULHO'
    if mesM==8:
        return 'AGOSTO'
    if mesM==9:
        return 'SETEMBRO'
    if mesM==10:
        return 'OUTUBRO'
    if mesM==11:
        return 'NOVEMBRO'
    if mesM==12:
        return 'DEZEMBRO'

def cidades_aniversario(lista, diaD, mesM):
    resultados = []
    for info_cidades in lista:
        if info_cidades[3] == diaD and info_cidades[4] == mesM:
            nome_uf = f'{info_cidades[2]}({info_cidades[0]})'
            resultados.append(nome_uf)
    return resultados

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
    dia, mes = int(input('')), int(input(''))

    #Processamento:
    cidades = carrega_cidades()
    cidades_selecionadas = cidades_aniversario(cidades, dia, mes)
    mes_digitado = mes_escrito(mes)

    #Saída:
    print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {mes_digitado}:')
    for cidades_escolhidas in cidades_selecionadas:
        print(cidades_escolhidas)
if __name__ == '__main__':
    main()
