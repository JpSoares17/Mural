def desconto(p):
    return 0.10*p

def main():
    p = float(input('Qual o valor do produto?').strip())
    pf = p - desconto(p)
    print(f'O valor final do produto com desconto é R$ {pf}')

if __name__ == '__main__':
    main()
