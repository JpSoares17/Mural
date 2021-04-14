def condicao(c):
    return ord(c) >= ord('0') and ord(c)<=ord('9')

def nega(c):
    return not condicao(c)

def main():
    c = input('Digite algo: ')
    print(f'É condição? {condicao(c)}', f'Não é condição? {nega(c)}', sep='.\n', end='.')

if __name__ == '__main__':
    main()
