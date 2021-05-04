def main():
    ns = input('')
    q = len(ns)
    ni = int(ns)
    x = []
    while True:
        k = ni//(10**(q-1))
        ni = ni%(10**(q-1))
        q -= 1
        x.append(k)
        if ni<10:
            x.append(ni)
        if ni<10: break
    x.reverse()
    for i in x:
        print(i, end='')
if __name__ == '__main__':
    main()
