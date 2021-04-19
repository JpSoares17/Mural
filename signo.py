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

def main():
    d = int(input(''))
    m = int(input(''))
    print(f'{cond(d, m)}')

if __name__ == '__main__':
    main()
