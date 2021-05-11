def desmb(n):
    s=0
    for i in range(7, 0, -1):
        s += n//10**i
        n = n%10**i
    s+=n
    return s

def main():
    n = int(input(''))
    print(desmb(n))
if __name__ == '__main__':
    main()
