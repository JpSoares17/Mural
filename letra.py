def let(c):
    return ord(c) >= ord('A') and ord(c) <= ord('Z')

def outr(c):
    return not let(c)

def main():
    c = input('Digite um caracter: ').upper()
    print(f'É letra: {let(c)}', f'Não é letra: {outr(c)}', sep='.\n', end='.')

if __name__ == '__main__':
    main()
