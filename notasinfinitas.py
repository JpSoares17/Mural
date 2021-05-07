def main():
        while True:
            n = float(input(''))
            if n>=0 and n<4:
                print('E')
                break
            if n>=4 and n<5:
                print('D')
                break
            if n>=5 and n<7:
                print('C')
                break
            if n>=7 and n<8.5:
                print('B')
                break
            if n>=8.5 and n<=10:
                print('A')
                break
            if not(0<=n<=10):
                print('Nota inválida.')
if __name__ == '__main__':
    main()
