def div(dv, dr):
    return dv//dr

def rest(dv, dr):
    return dv%dr

def main():
    dv = int(input('Dividendo: '))
    dr = int(input('Divisor: '))
    d = div(dv, dr)
    r = rest(dv, dr)
    print(f'{dv} dividido por {dr} é igual a {d} e resto {r}')

if __name__ == '__main__':
    main()
