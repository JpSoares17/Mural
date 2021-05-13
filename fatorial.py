def proc(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def main():
    n = int(input(''))
    print(proc(n))
if __name__ == '__main__':
    main()
