def letra(c):
    return ord(c) >= ord('A') and ord(c)<=ord('Z')

def num(c):
    return ord(c)>=ord('0') and ord(c)<=ord('9')

def vogal(c):
    if letra(c) and c in 'AEIOU':
        return c in 'AEIOU'

def con(c):
    if letra(c) and not vogal(c):
        return letra(c)
    elif letra(c) and vogal(c):
        return not vogal(c)
    else:
        return letra(c)


def main():
    c = input('Digite um caracter: ').upper()
    if num(c):
        print('Número')
    elif vogal(c):
        print('Vogal')
    elif con(c):
        print('Consoante')
    else:
        print('Símbolo')

if __name__ == '__main__':
    main()
