def gerar_agenda(numero_contatos):
    agenda = {}
    for codigo in range(numero_contatos):
        nome = input('').strip()
        cidade = input('').strip()
        estado = input('').strip()
        telefone = input('').strip()
        agenda[codigo] = (
            nome, cidade,
            estado, telefone)
    return agenda


def main():
    # Leitura:
    contatos = int(input(''))
    agenda = gerar_agenda(contatos)
    # Saída:
    for codigo in agenda:
        cidade = f'{agenda[codigo][1]}({agenda[codigo][2]})'
        print(f'{agenda[codigo][0]:<25}', end='')
        print(f'{cidade:<30}', end='')
        print(f'{agenda[codigo][3]:<}')


if __name__ == "__main__":
    main()
