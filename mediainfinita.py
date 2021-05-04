def main():
    n = 0
    q = 0
    while True:
        x = int(input(''))
        n += x
        q += 1
        if x==0: break
    if (q-1)!=0:
        print(f'{n/(q-1)}')

if __name__ == '__main__':
    main()
