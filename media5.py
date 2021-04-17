def media(n1, n2, n3, n4, n5):
    return (n1+n2+n3+n4+n5)/5

def main():
    n1 = float(input(''))
    n2 = float(input(''))
    n3 = float(input(''))
    n4 = float(input(''))
    n5 = float(input(''))
    
    x = []
    
    if n1>media(n1, n2, n3, n4, n5):
        x.append(n1)
    if n2>media(n1, n2, n3, n4, n5):
        x.append(n2)
    if n3>media(n1, n2, n3, n4, n5):
        x.append(n3)
    if n4>media(n1, n2, n3, n4, n5):
        x.append(n4)
    if n5>media(n1, n2, n3, n4, n5):
        x.append(n5)

    print(f'{media(n1, n2, n3, n4, n5):.2f}')

    for i in x:
        print('{:.2f}'.format(i))

if __name__ == '__main__':
    main()
