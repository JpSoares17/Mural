def sai(ma, me):
    if ma==0 or me==0:
        pass
    else:
        return f'{ma}\n{me}'

def process(n, ma, me):
    while True:
        nc = int(input(''))
        if nc>n and nc!=0:
            ma=nc
        if nc<n and nc!=0:
            me=nc
        if nc==0: break
    return ma, me

def main():
    n = int(input(''))
    ma, me = n, n
    ma, me = process(n, ma, me)
    print(sai(ma, me))

if __name__ == '__main__':
    main()
