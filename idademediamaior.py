def main():
    n = int(input(''))
    if n==0: quit()
    ma, me, s, q = n, n, n, 0
    while True:
        nc = int(input(''))
        s+=nc
        q+=1
        if nc>n and nc>ma and nc!=0:
            ma=nc
        if nc<n and nc<me and nc!=0:
            me=nc
        if nc==0: break
    m = s/q
    print('{}\n{:.2f}\n{}\n{}'.format(q, m, me, ma))

if __name__ == '__main__':
    main()
