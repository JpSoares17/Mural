def eh_par(n):
    return n%2 == 0

def eh_impar(n):
    return (not eh_par(n))

def main():
    n = int(input('Digite um número: '))
    print(f'É par: {eh_par(n)}', f'É ímpar: {eh_impar(n)}', sep='.\n', end='.')

if __name__ == '__main__':
    main()
