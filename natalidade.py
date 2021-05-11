def nat(a, b):
    ano=0
    x = max([a, b])
    y = min([a, b])
    while True:
        ano+=1
        x+=x*0.02
        y+=y*0.03
        if y>x: break
    return ano

def main():
    a, b = int(input('')), int(input(''))
    print(nat(a, b))
if __name__ == '__main__':
    main()
