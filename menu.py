def main():
    while True:
        o = int(input('OPÇÕES:\n1 - SAUDAÇÃO\n2 - BRONCA\n3 - FELICITAÇÃO\n0 - FIM\n'))
        if o==1:
            print('1 - Olá. Como vai?')
        if o==2:
            print('2 - Vamos estudar mais.')
        if o==3:
            print('3 - Meus Parabéns!')
        if o not in [0, 1, 2, 3]:
            print('Opção inválida.')
        if o==0:
            print('0 - Fim de serviço.')
            break
if __name__ == '__main__':
    main()
