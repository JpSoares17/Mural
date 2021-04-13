def eh_verde(s):
    return s=='V' or s=='VERDE'

def eh_amarelo(s):
    return s=='A' or s=='AMARELO'

def eh_vermelho(s):
    return s=='E' or s=='VERMELHO'

def main():
    s = input('Semáforo está: V-verde  A-amarelo  E-vermelho ').upper()
    print(f'Está verde: {eh_verde(s)}', f'Está amarelo: {eh_amarelo(s)}', f'Está vermelho: {eh_vermelho(s)}', sep='.\n', end='.\n')
    if eh_verde(s):
        print('Siga')

    elif eh_amarelo:
        print('Atenção')

    else:
        print('Pare')

if __name__ == '__main__':
    main()
