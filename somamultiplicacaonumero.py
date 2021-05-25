def multiplicacao(lista):
    multiplicacao_numero = 1
    for z in range(10):
        multiplicacao_numero *= lista[z]
    return multiplicacao_numero

def soma(lista):
    soma_numero = 0
    for t in range(10):
        soma_numero += lista[t]
    return soma_numero

def main():
    lista_numero = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(10):
        lista_numero[i] = int(input('Digite um número: '))
    numero_somado, numero_multiplicado = soma(lista_numero), multiplicacao(lista_numero)
    print(f'{lista_numero}\n{numero_somado}\n{numero_multiplicado}')
if __name__ == '__main__':
    main()
