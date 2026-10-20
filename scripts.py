from collections import deque
import heapq #estrutura de fila de prioridade




###BFS### (Breadth-First Search), ou Busca em Largura, explora os caminhos por níveis: 
#   primeiro os locais mais próximos do ponto inicial, depois os mais distantes
def bfs(grafo, inicio, saida):
    visitados = {inicio}
    fila = deque([inicio])

    # Guarda o nó anterior
    anteriores = {inicio: None}

    while fila:
        atual = fila.popleft()

        if atual == saida:
            break

        # Explora os vizinhos
        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                anteriores[vizinho] = atual
                fila.append(vizinho)

    # Verifica se a saída foi encontrada
    if saida not in anteriores:
        return [], len(visitados)

    # Reconstrói o caminho da saída até o início
    caminho = []
    atual = saida

    while atual is not None:
        caminho.append(atual)
        atual = anteriores[atual]

    # Inverte para começar pela entrada
    caminho.reverse()

    return caminho, len(visitados)


###DFS### DFS (Depth-First Search), ou Busca em Profundidade, segue um caminho o mais longe possível antes de voltar e tentar outro,
#  usando a recursão para explorar cada caminho até o fim antes de retroceder.

def dfs(grafo, inicio, saida):
    #Usa Estrutra de dados Set, para armazenar os nós visitados e evitar ciclos
    visitados = set()
    caminho = []
    #Recursao
    def buscar(atual):
        visitados.add(atual)  #registra os nós Descobertos
        caminho.append(atual) #resgistra a sequencia de nós
        # Verifica se a saída foi encontrada
        if atual == saida:
            return True

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                if buscar(vizinho):
                    return True

        caminho.pop()
        return False

    encontrou = buscar(inicio)

    if encontrou:
        return caminho, len(visitados)

    return [], len(visitados)


###Greedy Best-First Search### ou Busca Gulosa, prioriza a exploração dos nós com base em uma função heurística, que estima a distância até o objetivo.
def heuristica(casa, saida):
    # Calcula estimativa da distancia entre a casa e a saida
    #distância de Manhattan
    return abs(casa[0] - saida[0]) + abs(casa[1] - saida[1])


def greedy(grafo, inicio, saida):
    #Usa Estrutra de dados Set, para armazenar os nós visitados e evitar ciclos
    visitados = set()
    fila = []
    
    anteriores = {inicio: None}

    #BUsca a casa com menor distância estimada
    heapq.heappush(
        fila,
        (heuristica(inicio, saida), inicio)
    )

    while fila:
        _, atual = heapq.heappop(fila)


        if atual in visitados:
            continue

        visitados.add(atual)

        # Verifica se chegou à saída
        if atual == saida:
            break

        # Descobre os vizinhos ainda não registrados
        for vizinho in grafo[atual]:
            if vizinho not in anteriores:
                anteriores[vizinho] = atual

                heapq.heappush(
                    fila,
                    (heuristica(vizinho, saida), vizinho)
                )

    # Verifica se a saída foi encontrada
    if saida not in visitados:
        return [], len(visitados)

    # Reconstrói o caminho usando os predecessores, igual ao BFS
    caminho = []
    atual = saida

    while atual is not None:
        caminho.append(atual)
        atual = anteriores[atual]

    caminho.reverse()

    return caminho, len(visitados)