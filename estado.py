def reconhecimento(s):
    if s == 'SP':
        print("Paulista")

    elif s == 'CE':
        print("Cearense")

    elif s == 'MG':
        print("Mineiro")

    else:
        print("Outros Estados")

def main():
    try:
        s = str(input("Digite a sigla do seu Estado: ").upper())
        reconhecimento(s)

    except:
        print("Ocorreu algo de errado")

if __name__ == '__main__':
    main()
