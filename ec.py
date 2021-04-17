def main():
    n = input('')
    ec = int(input(''))
    x = []
    y = []
    if ec == 2:
        x.append(n)
        for i in x:
            print(len(i))
    elif ec == 1:
        n2 = input('')
        x.append(n)
        y.append(n2)
        for i in x:
            for w in y:
                print(len(i)+len(w))

if __name__ == '__main__':
    main()
