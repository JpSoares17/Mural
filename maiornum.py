def num():
    num = 0
    for i in range(100):
        n = int(input(''))
        if n>num:
            num = n
    return num

def main():
    print(num())

if __name__ == '__main__':
    main()
