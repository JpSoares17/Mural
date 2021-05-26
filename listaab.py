def intercalar(lista_1, lista_2):
    lista_3 = [*sum(zip(lista_1, lista_2), ())]
    return lista_3

def main():
    lista_a = []
    lista_b = []
    for i in range(25):
        #Leitura de A:
        elementos = int(input('Digite números: ').strip())
        lista_a.append(elementos)
    for j in range(25):
        #Leitura de B
        elements = int(input('Digite números: ').strip())
        lista_b.append(elements)
    #Processamento:
    lista_c = intercalar(lista_a, lista_b)

    #Saída:
    print(lista_a, lista_b, lista_c, sep='\n')
if __name__ == '__main__':
    main()
