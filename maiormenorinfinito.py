def main():
    ma=0
    x=[]
    q=0
    while True:
        n=int(input(''))
        x.append(n)
        if n>ma:
            ma=n
        q+=1
        if n==0: break
    del(x[q-1])
    if ma==0 or min(x)==0:
        pass
    else:
        print(f'{ma}\n{min(x)}')
if __name__ == '__main__':
    main()
