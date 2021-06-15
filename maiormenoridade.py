def menor(tabela):
    menor = {}
    for codigo in tabela:
        if tabela[codigo][1] < 18:
            menor[codigo] = tabela[codigo]
    return menor


def maior(tabela):
    maior = {}
    for codigo in tabela:
        if tabela[codigo][1] >= 18:
            maior[codigo] = tabela[codigo]
    return maior


def gerar_dicionario():
    geral = {}
    for codigo in range(20):
        nome = input('').strip()
        idade = int(input('').strip())
        cpf = input('').strip()
        geral[codigo] = (
            nome, idade,
            cpf)
    return geral


def main():
    # Leitura:
    tabela = gerar_dicionario()
    # Processamento:
    maior_idade = maior(tabela)
    menor_idade = menor(tabela)
    # Saída:
    print('========== MAIORES DE 18 ANOS ==========')
    for codigo in maior_idade:
        print(f'{maior_idade[codigo][0]};', end='')
        print(f'{maior_idade[codigo][1]};', end='')
        print(f'{maior_idade[codigo][2]}')
    print('========== MENORES DE 18 ANOS ==========')
    for codigo in menor_idade:
        print(f'{menor_idade[codigo][0]};', end='')
        print(f'{menor_idade[codigo][1]};', end='')
        print(f'{menor_idade[codigo][2]}')


if __name__ == '__main__':
    main()
