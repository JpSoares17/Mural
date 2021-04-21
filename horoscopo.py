def remover_acentos(texto):
    from unicodedata import normalize

    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

def horoscopo(signo):
    import urllib.request

    signo_formatado = remover_acentos(signo).lower()

    minha_url = 'https://www.horoscopovirtual.com.br/horoscopo/' + signo_formatado

    requisicao = urllib.request.Request(
        url = minha_url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    resposta = urllib.request.urlopen(requisicao)

    pagina = resposta.read().decode('utf-8')

    marcador_inicio = '<p class="text-pred">'
    marcador_final = '</p>'

    inicio = pagina.find(marcador_inicio) + len(marcador_inicio)
    final = pagina.find(marcador_final, inicio)

    return signo + ':' + pagina[inicio:final]

def cond(d, m):
    if (m==3 and d in range(21,32)) or (m==4 and d in range(1, 20)):
        return 'Áries'
    if (m==4 and d in range(20, 31)) or (m==5 and d in range(1, 21)):
        return 'Touro'
    if (m==5 and d in range(21, 32)) or (m==6 and d in range(1, 22)):
        return 'Gêmeos'
    if (m==6 and d in range(22, 31)) or (m==7 and d in range(1, 23)):
        return 'Câncer'
    if (m==7 and d in range(23, 32)) or (m==8 and d in range(1, 23)):
        return 'Leão'
    if (m==8 and d in range(23, 32)) or (m==9 and d in range(1, 23)):
        return 'Virgem'
    if (m==9 and d in range(23, 31)) or (m==10 and d in range(1, 23)):
        return 'Libra'
    if (m==10 and d in range(23, 32)) or (m==11 and d in range(1, 22)):
        return 'Escorpião'
    if (m==11 and d in range(22, 31)) or (m==12 and d in range(1, 22)):
        return 'Sagitário'
    if (m==12 and d in range(22, 32)) or (m==1 and d in range(1, 20)):
        return 'Capricórnio'
    if (m==1 and d in range(20, 32)) or (m==2 and d in range(1, 19)):
        return 'Aquário'
    if (m==2 and d in range(19, 31)) or (m==3 and d in range(1, 21)):
        return 'Peixes'

def separar_data(dma):
    a = dma%10000
    dma //= 10000

    m = dma%100
    dma //= 100

    d = dma
    return d, m, a

def main():
    nascimento = int(input(''))
    dia, mes, ano = separar_data(nascimento)
    meu_signo = cond(dia, mes)
    horoscopo_de_hoje = horoscopo(meu_signo)
    print(horoscopo_de_hoje)

if __name__ == '__main__':
    main()
