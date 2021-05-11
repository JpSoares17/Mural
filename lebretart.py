def vel(d):
    dl=0
    m=0
    while d!=dl:
        m+=1
        d+=1
        dl+=10
        if d<=dl: break
    return m

def main():
    d=float(input(''))
    print(vel(d))
if __name__ == '__main__':
    main()
