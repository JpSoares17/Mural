def media_aluno(alunos, chaves):
    medias = []
    for chave in chaves:
        media = (alunos[chave][1] + alunos[chave][2])/2
        media_formatada = f'{alunos[chave][0]}: {media:.1f}'
        medias.append(media_formatada)
    return medias


def pesquisa():
    chaves = []
    while True:
        chave = input('').strip()
        if chave == '':
            break
        chaves.append(chave)
    return chaves


def leitura_alunos():
    alunos = {}
    while True:
        matricula = input('').strip()
        if matricula == '':
            break
        nome = input('').strip()
        nota_1 = float(input('').strip())
        nota_2 = float(input('').strip())
        alunos[matricula] = (
            nome, nota_1,
            nota_2)
    return alunos


def main():
    # Leitura:
    tabela_alunos = leitura_alunos()
    matriculas = pesquisa()
    # Processamento:
    medias_alunos = media_aluno(tabela_alunos, matriculas)
    # Saída:
    for aluno in medias_alunos:
        print(aluno)


if __name__ == "__main__":
    main()
