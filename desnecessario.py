def soma(lista):
    numeros_somados = 0
    for m in lista:
        numeros_somados += m
    return numeros_somados

def maximo(lista):
    maior_numero = 0
    for l in lista:
        if l>maior_numero:
            maior_numero = l
    return maior_numero

def minimo(lista):
    menor_numero = lista[0]
    for k in lista:
        if k<menor_numero:
            menor_numero = k
    return menor_numero

def reverter_lista(lista, numero_de_itens):
    lista_reversa = []
    for j in range(numero_de_itens):
        lista_reversa.append(0)
        lista_reversa[j] = lista[-(j+1)]
    return lista_reversa

def contador_itens_lista(lista):
    contador = 0
    for i in lista:
        contador +=1
    return contador

def main():
    #Entrada:
    minha_lista = []
    while True:
        itens = int(input('Digite um número: '))
        if itens == 0:
            break
        minha_lista.append(itens)

    #Processamento:
    quantidade_itens_lista = contador_itens_lista(minha_lista)
    minha_lista_reversa = reverter_lista(minha_lista, quantidade_itens_lista)
    menor_numero = minimo(minha_lista)
    maior_numero = maximo(minha_lista)
    numeros_somados = soma(minha_lista)

    #Saída:
    print(minha_lista, quantidade_itens_lista, minha_lista_reversa, menor_numero, maior_numero, numeros_somados, sep='\n')
    
if __name__ == '__main__':
    main()
