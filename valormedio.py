def main():
    num = 0
    for i in range(100):
        n = int(input(''))
        num += n
    med = num/100
    print('{:.2f}'.format(med))

if __name__ == '__main__':
    main()
