#Imports
from labirinto import labirinto, achar, montar_grafo, desenhar
from scripts import bfs, dfs, greedy


inicio = achar(labirinto, 'I')
saida = achar(labirinto, 'F')
grafo = montar_grafo(labirinto)

caminho_dfs, visitadas_dfs = dfs(grafo, inicio, saida)

print("Caminho encontrado pela DFS:")
desenhar(labirinto, caminho_dfs)

print("Tamanho do caminho:", len(caminho_dfs))
print("Casas visitadas:", visitadas_dfs)

print('')
print('')

caminho_bfs, visitadas_bfs = bfs(grafo, inicio, saida)

print("\nCaminho encontrado pela BFS:")
if caminho_bfs:
    desenhar(labirinto, caminho_bfs)
    print("Tamanho do caminho:", len(caminho_bfs))
else:
    print("Nenhum caminho encontrado.")

print("Casas visitadas:", visitadas_bfs)

print('')
print('')


caminho_greedy, visitadas_greedy = greedy(
    grafo, inicio, saida
)

print("\nCaminho encontrado pela Greedy Search:")
if caminho_greedy:
    desenhar(labirinto, caminho_greedy)
    print("Tamanho do caminho:", len(caminho_greedy))
else:
    print("Nenhum caminho encontrado.")

print("Casas visitadas:", visitadas_greedy)

print("Coordenadas do caminho da Greedy:")
print(caminho_greedy)