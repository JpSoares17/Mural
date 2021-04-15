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
    dh = int(input(''))
    mh = int(input(''))
    ah = int(input(''))
    da = int(input(''))
    ma = int(input(''))
    aa = int(input(''))
    print(f'{condicao(ma, mh, da, dh, ah, aa)}')

if __name__ == '__main__':
    main()
