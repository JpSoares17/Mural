def main():
    x = [] 
    n1, n2 = int(input('')), int(input(''))
    for i in range(n1, n2+1):
        x.append(i)
    for a in x:
        np=0
        for b in range(a-1, 1, -1):
            if a%b==0 and a!=2:
                np+=1
        if np==0:
            print(f'{a}')
    
if __name__ == '__main__':
    main()
