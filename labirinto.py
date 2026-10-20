labirinto = [
    "I..#......",
    ".#.#.####.",
    ".#...#....",
    ".#####.##.",
    ".....#....",
    "###..#.##..",
    "...#......",
    ".#.####.##.",
    ".#........",
    "...######F",
]

# Ordem dos movimentos: cima, direita, baixo e esquerda
DIRECOES = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def achar(lab, simbolo):
    for i, linha in enumerate(lab):
        if simbolo in linha:
            return (i, linha.index(simbolo))
    return None


def livre(lab, i, j):
    dentro = (
        0 <= i < len(lab)
        and 0 <= j < len(lab[i])
    )

    return dentro and lab[i][j] != '#'


def montar_grafo(lab):
    grafo = {}

    for i in range(len(lab)):
        for j in range(len(lab[i])):
            if not livre(lab, i, j):
                continue

            grafo[(i, j)] = []

            for di, dj in DIRECOES:
                ni = i + di
                nj = j + dj

                if livre(lab, ni, nj):
                    grafo[(i, j)].append((ni, nj))

    return grafo


def desenhar(lab, caminho):
    grade = [list(linha) for linha in lab]

    for i, j in caminho:
        if grade[i][j] == '.':
            grade[i][j] = '*'

    for linha in grade:
        print(''.join(linha))