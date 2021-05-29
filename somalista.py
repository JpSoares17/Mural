def soma_lista(lista_1, lista_2):
    lista_3 = zip(lista_1, lista_2)
    soma = [item_1+item_2 for (item_1, item_2) in lista_3]
    return soma

def main():
    #Leitura:
    lista_a = []
    lista_b = []
    for i in range(20):
        itens_a = int(input('Digite um número: '))
        lista_a.append(itens_a)
    for j in range(20):
        itens_b = int(input('Digite um número: '))
        lista_b.append(itens_b)

    #Processamento:
    lista_c = soma_lista(lista_a, lista_b)

    #Saída:
    print(lista_a, lista_b, lista_c, sep='\n')
if __name__ == '__main__':
    main()
