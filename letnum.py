def let(c):
    return ord(c) <= ord('Z') and ord(c) >= ord('A')

def num(c):
    return ord(c)<= ord('9') and ord(c) >= ord('0')

def n_cond(c):
    return not(let(c) or num(c))

def main():
    c = input('Digite um caracter: ').upper()
    print(f'É letra ou número: {let(c) or num(c)}', f'Não é letra ou número: {n_cond(c)}', sep='.\n', end='.')

if __name__ == '__main__':
    main()
