def par(lista_cheia):
    lista_base = []
    for y in lista_cheia:
        if y%2 == 0:
            lista_base.append(y)
    return lista_base

def impar(lista_cheia):
    lista_base = []
    for x in lista_cheia:
        if x%2 != 0:
            lista_base.append(x)
    return lista_base

def main():
    #Entrada:
    lista_total = []
    for i in range(20):
        numero = int(input(''))
        lista_total.append(numero)

    #Processamento:
    lista_impar = impar(lista_total)
    lista_par = par(lista_total)

    #Saída:
    print(lista_total, lista_par, lista_impar, sep='\n')
if __name__ == '__main__':
    main()
