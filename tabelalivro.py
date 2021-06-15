def gerar_tabela():
    dicionario = {}
    codigo = 100
    while True:
        codigo += 1
        titulo = input('').strip()
        if titulo == '':
            break
        isbn = input('').strip()
        autor = input('').strip()
        preco = float(input('').strip())
        dicionario[codigo] = (
            titulo, isbn,
            autor, preco)
    return dicionario


def main():
    # Leitura:
    tabela_livro = gerar_tabela()
    # Saída:
    for codigo in tabela_livro:
        print(f'Código: {codigo}')
        print(f'Título: {tabela_livro[codigo][0]}')
        print(f'ISBN: {tabela_livro[codigo][1]}')
        print(f'Autor: {tabela_livro[codigo][2]}')
        print(f'Preço: {tabela_livro[codigo][3]:.2f}')


if __name__ == "__main__":
    main()
