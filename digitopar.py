def desm_num(n):
    u = n%10
    n1 = n//10
    d = n1%10
    c = n1//10
    return c, d, u

def main():
    x = 0
    n = int(input(''))
    c, d, u = desm_num(n)
    if n>=100 and n<=999 and c%2==0:
        x +=1
    if n>=100 and n<=999 and d%2==0:
        x +=1
    if n>=100 and n<=999 and u%2==0:
        x +=1
        print(f'{x}')
    if n>=100 and n<=999 and c%2!=0:
        x+=0
    if n>=100 and n<=999 and d%2!=0:
        x+=0
    if n>=100 and n<=999 and u%2!=0:
        x+=0
        print(f'{x}')
    else:
        x +=0

if __name__ == '__main__':
    main()
