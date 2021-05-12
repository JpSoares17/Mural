def main():
    p = int(input(''))
    k = p*0.95
    a = 1600
    m = p*0.06
    n = p*0.01
    t = p*0.95
    while True:
        print('{:.0f},{:.0f},{:.0f},{:.0f}'.format(a, n, m, t))
        a+=1
        m -= 0.05*m
        n -= 0.05*n
        t *= 0.95
        if t<k*0.1: break
if __name__ == '__main__':
    main()
