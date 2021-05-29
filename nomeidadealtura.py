def media_altura(lista):
    return sum(lista)/len(lista)

def selecao(lista, lista_2, media):
    posicoes = []
    for (j, l, k) in zip(lista, lista_2, range(30)):
        if j>13 and l<media:
            posicoes.append(k)
    return posicoes

def main():
    #Leitura:
    lista_nomes = []
    lista_idades = []
    lista_alturas = []
    for i in range(30):
        item_nome = input('')
        lista_nomes.append(item_nome)
        item_idade = int(input(''))
        lista_idades.append(item_idade)
        item_altura = float(input(''))
        lista_alturas.append(item_altura)

    #Processamento:
    media_alturas = round(media_altura(lista_alturas), 2)
    selecionados = selecao(lista_idades, lista_alturas, media_alturas)

    #Saída:
    print('MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA')
    for m in selecionados:
        print(lista_nomes[m])
if __name__ == '__main__':
    main()
