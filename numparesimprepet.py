def eh_par(n):
    return n%2==0

def main():
    num_par = 0
    num_imp = 0
    for i in range(100):
        n = int(input(''))
        if eh_par(n):
            num_par +=1
        else:
            num_imp +=1

    print(f'{num_par}\n{num_imp}')

if __name__ == '__main__':
    main()
