def idade(ah, aa):
    return ah-aa

def condicao(ma, mh, da, dh, ah, aa):
    if ma==mh and da>dh:
        return (idade(ah, aa)-1)
    elif ma>mh:
        return (idade(ah,aa)-1)
    elif ma<mh:
       return idade(ah,aa)
    elif ma == mh and da<=dh:
        return idade(ah, aa)
def main():
    dh = int(input('Digite o dia atual: '))
    mh = int(input('Digite o mês atual: '))
    ah = int(input('Digite o ano atual: '))
    da = int(input('Digite o dia do seu aniversário: '))
    ma = int(input('Digite o mês do seu aniversário: '))
    aa = int(input('Digite o ano do seu aniversário: '))
    print(f'Sua idade é {condicao(ma, mh, da, dh, ah, aa)}')

if __name__ == '__main__':
    main()
