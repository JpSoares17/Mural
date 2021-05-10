def main():
    s, d = float(input('')), float(input(''))
    m = 10
    a = 2016
    while True:
        m+=1
        d=1.15*d
        if m>12:
            m=1
            a+=1
        if m == 3:
            s= 1.05*s
        if d>s: break
    print(f'{m}/{a}')
if __name__ == '__main__':
    main()
