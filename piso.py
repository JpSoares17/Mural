def cal(l, c, a):
    ap = l*c
    vs = l*c*a
    aps = 2*a*l+2*a*c
    return ap, vs, aps

def main():
    l, c, a = float(input('')), float(input('')), float(input(''))
    print(cal(l, c, a))
if __name__ == '__main__':
    main()
