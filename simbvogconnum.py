def letra(c):
    return ord(c) >= ord('A') and ord(c) <= ord('Z')

def num(c):
    return ord(c)>=ord('0') and ord(c)<=ord('9')

def vog(c):
    return c in 'AEIOU'

def con(c):
    if letra(c) and not(vog(c)):
        return letra(c)
    elif not letra(c):
        return letra(c)
    else:
        return not(vog(c))

def sim(c):
    if not(letra(c)) and not(num(c)):
        return not(letra(c))
    else:
        return not(letra(c)) and not(num(c))

def main():
    c = input('Digite um caracter: ').upper()
    print(f'É vogal: {vog(c)}', f'É consoante: {con(c)}', f'É número: {num(c)}', f'É símbolo: {sim(c)}', sep='.\n', end='.')

if __name__ == '__main__':
    main()
