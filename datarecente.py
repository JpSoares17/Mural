def data1(d1, m1, a1):
    return f'{d1}/{m1}/{a1}'

def data2(d2, m2, a2):
    return f'{d2}/{m2}/{a2}'

def cond(d1, d2, m1, m2, a1, a2):
    if a1>a2:
        return data1(d1, m1, a1)
    elif a2>a1:
        return data2(d2, m2, a2)
    elif a1==a2 and m1>m2:
        return data1(d1, m1, a1)
    elif a1==a2 and m2>m1:
        return data2(d2, m2, a2)
    elif a1==a2 and m1==m2 and d1>d2:
        return data1(d1, m1, a1)
    elif a1==a2 and m1==m2 and d2>d1:
        return data2(d2, m2, a2)
    else:
        return data1(d1, m1, a1)
def main():
    d1 = int(input(''))
    m1 = int(input(''))
    a1 = int(input(''))
    d2 = int(input(''))
    m2 = int(input(''))
    a2 = int(input(''))
    print(f'{cond(d1, d2, m1, m2, a1, a2)}')

if __name__ == '__main__':
    main()
    
