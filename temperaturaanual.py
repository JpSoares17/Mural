def selecao_de_temperaturas(matriz, media_temp):
    temperaturas_selecionadas = []
    for i_linhas in range(len(matriz)):
        if matriz[i_linhas][1] > media_temp:
            temperaturas_selecionadas.append(matriz[i_linhas])
    return temperaturas_selecionadas


def media(matriz):
    soma = 0
    for i_linhas in range(len(matriz)):
        soma += matriz[i_linhas][1]
    return soma/len(matriz)


def conversao_temperaturas(matriz):
    for i_linhas in range(len(matriz)):
        if matriz[i_linhas][2] == 'F':
            matriz[i_linhas][1] = round(
                conversao_farenheit(matriz[i_linhas][1]), 2)
            matriz[i_linhas][2] = 'K'
        if matriz[i_linhas][2] == 'C':
            matriz[i_linhas][1] = round(
                conversao_celsius(matriz[i_linhas][1]), 2)
            matriz[i_linhas][2] = 'K'
    return matriz


def conversao_celsius(temperatura):
    return temperatura+273.15


def conversao_farenheit(temperatura):
    return (temperatura + 459.67)/1.8


def meses(numero_do_mes):
    meses_listados = (
        'Janeiro', 'Fevereiro', 'Março',
        'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro',
        'Outubro', 'Novembro', 'Dezembro')
    return meses_listados[numero_do_mes]


def preencher_temperaturas(linhas, elementos):
    matriz = []
    for linha in range(linhas):
        vetor = []
        mes = meses(linha)
        temperatura = float(input(''))
        escala = input('').upper().strip()
        vetor.append(mes)
        vetor.append(temperatura)
        vetor.append(escala)
        matriz.append(vetor)
    return matriz


def main():
    # Leitura:
    temperaturas = preencher_temperaturas(12, 1)
    # Processamento:
    temperaturas_convertidas = conversao_temperaturas(temperaturas)
    media_das_temperaturas = round(media(temperaturas_convertidas), 2)
    temperaturas_acima_da_media = selecao_de_temperaturas(
        temperaturas_convertidas, media_das_temperaturas)
    # Saída:
    print('TEMPERATURA MÉDIA ANUAL')
    print(f'{media_das_temperaturas}K')
    print('TEMPERATURAS ACIMA DA MÉDIA ANUAL:')
    for i_linhas in range(len(temperaturas_acima_da_media)):
        print(f'{temperaturas_acima_da_media[i_linhas][0]}: ', end='')
        print(f'{temperaturas_acima_da_media[i_linhas][1]}K')


if __name__ == '__main__':
    main()
