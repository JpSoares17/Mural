def desconto(dias):
    return dias*5

def main():
    di = int(input("Quantos dias de atraso? ").strip())
    desc = desconto(di)
    nf = 100 - desc
    print("Sua nota final ficou %.2f" %nf)

if __name__ == '__main__':
    main()
