def proc(n):
    np=0
    for i in range(n-1, 1, -1):
        if n%i==0 and n!=2:
            np+=1
    if np==0:
        return np==0
    else:
        return np==0

def main():
    n=int(input(''))
    print(proc(n))
if __name__ == '__main__':
    main()
