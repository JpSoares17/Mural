def min_h(minu):
    h = minu//60
    m = minu%60
    return h, m

def main():
    minu = int(input('Quantos minutos quer converter? '))
    h, m = min_h(minu)
    print(f'{minu} equivale a {h}h e {m}min')

if __name__ == '__main__':
    main()
