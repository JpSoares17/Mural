def truncamento_2casas(numbers):
    return float('{:.2f}'.format(numbers))

def truncamento_4casas(numbers):
    return float('{:.4f}'.format(numbers))

def medias(numbers, soma_numbers):
    if numbers == 0:
        return 0
    if numbers != 0:
        return soma_numbers/numbers

def letras(numbers):
    quantidade_de_vogais = 0
    lista_base = []
    for x in range(numbers):
        letra = input('Digite letras: ').strip()
        if letra in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
            quantidade_de_vogais+=1
        else:
            lista_base.append(letra)
    return lista_base, quantidade_de_vogais

def notas(number):
    lista_base = []
    soma_notas = 0
    for y in range(number):
        nota = float(input('Digite notas: '))
        nota = truncamento_2casas(nota)
        soma_notas += nota
        lista_base.append(nota)
    if number == 0:
        return lista_base, soma_notas
    else:
        return lista_base, soma_notas

def reais(number):
    lista_base = []
    for i in range(number):
        numeros = float(input('Digite números: '))
        numeros = truncamento_4casas(numeros)
        lista_base.append(numeros)
    lista_base.reverse()
    return lista_base

def main():
    #Entrada:
    numero = int(input('Quantidade de termos: '))
    
    #Processamento:
    lista_real = reais(numero)
    lista_notas, minha_soma_notas = notas(numero)
    media = medias(numero, minha_soma_notas)
    lista_letra, quantidade_vogais = letras(numero)

    #Saída:
    print(lista_real, lista_notas, sep='\n', end='\n')
    if numero == 0:
        print('SEM NOTAS')
    else:
        print(f'{media:.1f}')
    print(quantidade_vogais, lista_letra, sep='\n')
if __name__ == '__main__':
    main()
