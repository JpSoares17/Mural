def trans(h, m, s):
    return h*3600+m*60+s

def main():
    h = int(input(''))
    m = int(input(''))
    s = int(input(''))
    print(trans(h, m ,s))

if __name__ == '__main__':
    main()
