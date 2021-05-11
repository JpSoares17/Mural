def cont(p):
    m=0
    pop=10000
    while True:
        m+=1
        pop+=pop*0.007
        p+=p*0.004
        if pop>=p: break
    return m

def main():
    p=float(input(''))
    print(cont(p))
if __name__ == '__main__':
    main()
