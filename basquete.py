def alturas_acima_media(lista_1, lista_2, media):
    posicoes = []
    lista_1_selecionados = []
    lista_2_selecionados = []
    for (l, m) in zip(lista_1, range(12)):
        if l>media:
            posicoes.append(m)
    for n in posicoes:
        lista_1_selecionados.append(lista_1[n])
        lista_2_selecionados.append(lista_2[n])
    return lista_1_selecionados, lista_2_selecionados
            

def intercalando(lista_1, lista_2):
    intercalada = []
    for a, b in zip(lista_1, lista_2):
        intercalada.append(a)
        intercalada.append(b)
    return intercalada

def posicao(lista_1):
    numero_posicao = 0
    for j, k in zip(lista_1, range(24)):
        if lista_1[k] == max(lista_1):
            break
        numero_posicao +=1
    return numero_posicao
    
def media_das_alturas(lista):
    media = sum(lista)/len(lista)
    return media

def main():
    #Leitura:
    lista_nomes = []
    lista_alturas = []
    for i in range(12):
        item_nome = input('Nome do jogador: ')
        lista_nomes.append(item_nome)
        item_altura = float(input('Altura do jogador: '))
        lista_alturas.append(item_altura)

    #Processamento:
    media_altura = media_das_alturas(lista_alturas)
    maior_altura = max(lista_alturas)
    lista_geral = intercalando(lista_nomes, lista_alturas)
    posicao_nome_altura = posicao(lista_alturas)
    nome_jogador = lista_nomes[posicao_nome_altura]
    lista_nomes_selecionados, lista_alturas_selecionados = alturas_acima_media(lista_alturas, lista_nomes, media_altura)
    

    #Saída:
    print('JOGADOR MAIS ALTO DO TIME')
    print(nome_jogador)
    print('{:.2f}'.format(maior_altura))
    print('ALTURA MÉDIA DO TIME')
    print('{:3.2f}'.format(media_altura))
    print('JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')
    for (o, p) in zip(lista_nomes_selecionados, lista_alturas_selecionados):
        print(p, '{:.2f}'.format(o), sep='\n')
if __name__ == '__main__':
    main()
