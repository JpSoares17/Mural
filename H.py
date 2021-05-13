def proces(n):
    s1=1
    s2=0
    x=0
    while True:
        s2+=1
        x+=s1/s2
        if s2 == n: break
    return x

def main():
    n=int(input(''))
    k = proces(n)
    print('{:.4f}'.format(k))
if __name__ == '__main__':
    main()
