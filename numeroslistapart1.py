def reverter(number):
    lista_base = []
    for y in range(number):
        numeros = int(input('Digite números: '))
        lista_base.append(numeros)
    lista_base.reverse()
    return lista_base

def leitura(number):
    lista_base = []
    for y in range(number):
        numeros = int(input('Digite números: '))
        lista_base.append(numeros)
    return lista_base

def sequencia(number):
    lista_base = []
    for z in range(number):
        lista_base.append(z+1)
    return lista_base

def listazero(number):
    lista_base = []
    for i in range(number):
        lista_base.append(0)
    return lista_base

def main():
    
    #Entrada:
    numero = int(input('Quantidade de membros da elementos: '))

        
    #Processamento:
    lista_zero = listazero(numero)
    lista_sequencia = sequencia(numero)
    lista_leitura = leitura(numero)
    lista_reversa = reverter(numero)

    
    #Saída:
    print(lista_zero, lista_sequencia, lista_leitura, lista_reversa, sep='\n')
if __name__ == '__main__':
    main()
