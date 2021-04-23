def media(n1, n2, n3):
    return (n1+n2+n3)/3

def cond(n1, n2, n3):
    if n3>8:
        return media(n1, n2, n3)+1
    if media(n1, n2, n3)>10:
        return 10
    else:
        return media(n1, n2, n3)

def main():
    n1, n2, n3 = float(input('')), float(input('')), float(input(''))
    print(cond(n1, n2, n3))

if __name__ == '__main__':
    main()
