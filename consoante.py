def letra(c):
    return ord(c)>=ord('A') and ord(c)<=ord('Z')

def con(c):
    if letra(c):
        return c not in 'AEIOU'
    elif not letra(c):
        return letra(c)

def n_con(c):
        if letra(c) and not con(c):
            return not con(c)
        elif not letra(c):
            return not letra(c)
        elif con(c):
            return not con(c)

def main():
    c = input('Digite um caracter: ').upper()
    print(f'É consoante: {con(c)}', f'Não é consoante: {n_con(c)}', sep='.\n', end='.')

if __name__ == '__main__':
    main()
