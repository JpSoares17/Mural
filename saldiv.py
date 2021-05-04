def main():
    s = float(input(''))
    d = float(input(''))
    m = 10
    a = 2016
    while True:
        m +=1
        if m==13:
            m = 1
            a += 1
        if m==3:
            s = s+s*0.05
        d = d+d*0.15
        if d>s: break
    print(f'{m}/{a}')
if __name__ == '__main__':
    main()
