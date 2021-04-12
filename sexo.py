def main():
    try:
        n = input("Qual seu nome? ").strip()
        s = int(input("Qual seu sexo? 1 - Masculino  2 - Feminino "))
        if s == 1:
            print("Ilmo Sr. %s" %n)

        if s == 2:
            print("Ilma Sra. %s" %n)

    except:
        print("Digite um valor válido.")
        main()

if __name__ == '__main__':
    main()
