def main():
    try:
        n = input("").strip()
        s = int(input(""))
        if s == 1:
            print("Ilmo Sr. %s" %n)

        if s == 2:
            print("Ilma Sra. %s" %n)

    except:
        print("Digite um valor válido.")
        main()

if __name__ == '__main__':
    main()
