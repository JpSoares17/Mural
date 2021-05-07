def main():
    s=0
    q=0
    while True:
        print('CÓDIGO  PRODUTO         PREÇO (R$)')
        print('H       Hamburger       5,50')
        print('C       Cheeseburger    6,80')
        print('M       Misto Quente    4,50')
        print('A       Americano       7,00')
        print('Q       Queijo Prato    4,00')
        print('X       PARA TOTAL DA CONTA')
        n = input('').upper()[0]
        q+=1
        if n=='H':
            s+=5.5
        if n=='C':
            s+=6.8
        if n=='M':
            s+=4.5
        if n=='A':
            s+=7
        if n=='Q':
            s+=4
        if n not in ['H', 'C', 'M', 'A', 'Q', 'X']:
            print('Opção inválida.')
        if n=='X':
            print('{:.2f}'.format(s))
            break
if __name__ == '__main__':
    main()
