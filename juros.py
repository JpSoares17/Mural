def main():
    q = 0
    x = float(input(''))
    j = float(input(''))
    while True:
        m = x*(1+j/100)**q
        q += 1
        if m >= x*2: break
    print(f'{q-1}')

if __name__ == '__main__':
    main()
