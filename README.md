Entedimento sobre os Algoritimos Aplicados:

1 - BFS:
A Breadth-First Search ou apenas Busca em Largura, Explora os nós analisados por nivel, primeiro os locais mais próximos do ponto inicial, depois os mais distantes. Ela basicante pega um nó que esta na fila, quarda ele, e parte para verificar o nó vizinho, adicionando a filas os que não foram visitados.
Ela é muito eficiente para econtrar caminhos curtos, apenas quando o grafo não possui pesos.

2 - DFS:
Depth-First Search, ou Busca em Profundidade, Segue um caminho até o maximo possivel. Para após começar a explorar outros caminhos utilizando a recursividade. Ela segue um dos caminhos ate o final e verifica se chegou no obejivo (no nosso caso o final do labirinto), se não chegar, parte para o vizinho que não foi visitado e chama a funçao novamente, caso nao chega ainda ao objetivo, repete o processo anterior, chamando a funcao recursiva.
Através dele pode-se encontrar o objetivo sem ir em todos os caminhos, mas não necessariamente é o menor caminho.

3 - Greedy Search
A Greedy Search utiliza a heurística, a partir da formula distância de Manhattan dela cria uma maneira de estimar a distancia estimade entre um nó e outro.
o algoritmo calcula a estimativa de distância dos vizinhos até o objetivo, a partir da lista de prioridade do objetivo ela selcione oq parece estar mais proximo. Repetindo o processo ate encontrar o destino ou ent esgotar a possibilidades.
Ela pode chegar de maneira veloz ao objetivo, porém nao garante o menor caminho. Por conta da estimativa.

Por que a BFS encontrou o menor caminho e a DFS não?
Por conta que  verifica os nós mais proximos e o grafo possui o mesmo peso, sendo assim verificando as posicições mais proximas.
Diferente da DFS, que segue um caminho todo, para depois verificar o resto.

Em que ponto do labirinto a Busca Gulosa foi induzida a um caminho inadequado por uma parede?
Ela pode ser induzida a um caminho inadequado quando escolhe uma posição aparentimente mais proxima do final, mas possui uma parede logo após, no labirindo criado para o exercicio isso ocorre na regial central, que está proxima e F (final) mas tem obstaculos logo após.
Labirinto:

O labirinto foi desenvolvido utilizando a estrutura de dados de Lista e matriz, mantendo a proporção indicada.
I Representa Inicio, F o Final, os # seriam as paredes do labirinto e os pontos sao os caminhos livres.
Que representam os nós (comentados anteriormente), e os movimentos sao defininos em 4 direcoes,
cima, baixo, direita e esquerda.



