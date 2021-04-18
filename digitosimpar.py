def dems_num(n):
    d = n//10
    u = n%10
    return d, u

def main():
    n = int(input(''))
    x = 0
    d, u = dems_num(n)
    if n>=10 and n<=99 and d%2!= 0 and u%2!=0:
        print(f'Os dois dígitos são ímpares.')
    if (n>=10 and n<=99 and d%2==0 and u%2!=0) or (n>=10 and n<=99 and d%2!= 0 and u%2==0):
        print(f'Apenas um dígito é ímpar.')
    if  n>=10 and n<=99 and d%2== 0 and u%2==0:
        print(f'Nenhum dígito é ímpar.')
    else:
        pass


if __name__ == '__main__':
    main()
