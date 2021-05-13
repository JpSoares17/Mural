def fibonacci(n):
    q=2
    p=0
    s=1
    print(f'{p}, {s}', end='')
    while True:
        q+=1
        prox= p+s
        p=s
        s=prox
        print(f', {s}', end='')
        if q == n: break

def main():
    n = int(input(''))
    fibonacci(n)
if __name__ == '__main__':
    main()
