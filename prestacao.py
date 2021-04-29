def main():
    n = float(input(''))
    for i in range(1, 25):
        k = n/i
        print('{:.0f}x de R$ {:.2f}'.format(i, k))

if __name__ == '__main__':
    main()
