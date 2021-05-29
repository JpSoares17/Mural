def contador(lista, numero_contado):
    vezes_repetidas = 0
    for i in lista:
        if i==numero_contado:
            vezes_repetidas+=1
    return vezes_repetidas

def main():
    #Leitura:
    lista_leitura = []
    while True:
        itens = int(input('Digite um número: '))
        if itens == 0: break
        lista_leitura.append(itens)
    item_contagem = int(input('Que número quer saber quantas vezes repetiu?'))

    #Processamento:
    quantidades_repetidas = contador(lista_leitura, item_contagem)

    #Saída:
    print(lista_leitura, item_contagem, quantidades_repetidas, sep='\n')
if __name__ == '__main__':
    main()
