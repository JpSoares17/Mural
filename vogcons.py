#Reconhece se o caracter é letra ou não
def let(c):
    return ord(c) >= ord('A') and ord(c)<=ord('Z')

#Reconhece se o caracter é número
def num(c):
    return ord(c) >= ord('0') and ord(c)<=ord('9')

#Se ele for letra, vai reconhecer se é vogal ou não
def vog(c):
    if let(c) and c in 'AEIOU':
        return c in'AEIOU'

#Se for letra, vai reconhecer se é consoante ou não
def con(c):
    if let(c) and not(vog(c)):
        return not(vog(c))

def main():
    #Entrada de dados
    c = input('Digite um caracter: ').upper()
     #Processamento e saída de dados num código só
    print(f'É letra: {let(c)}', f'É número: {num(c)}', f'É vogal: {vog(c)}', f'É consoante: {con(c)}', sep='.\n', end='.')

if __name__ == '__main__':
    main()
