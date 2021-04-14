def md(n1, n2, n3):
    return (n1+n2+n3)/3

def main():
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nota: '))
    m = md(n1, n2, n3)
    if n3>8:
        m=m+1
    if m>10:
        m=10
    print(f'{m}')

if __name__ == '__main__':
    main()
