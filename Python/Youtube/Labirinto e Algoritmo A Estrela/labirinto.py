from pyamaze import maze, agent, textLabel

labirinto = maze() #labirinto perfeito, com apenas um caminho, tamanho 10linhas x 10colunas e qualquer celula te leva ao final

labirinto.CreateMaze(loadMaze="C:/Users/carol/Documents/Repositorios GitHub/03_Hashtag/Python/Youtube/Labirinto e Algoritmo A Estrela/maze--2024-02-11--22-39-48.csv")
#labirinto.CreateMaze(loopPercent=50) # quantidade de caminhos para completar o labirinto (padrão 0)
# celulas = labirinto.grid
# print(celulas)

# mapa = labirinto.maze_map
# print(mapa)

# caminho = labirinto.path #gabarito
# print(caminho)

agente = agent(labirinto, footprints=True, filled=True)
# caminho = {(10, 10): (10, 9), (10, 9): (10, 8), (10, 8): (9, 8)}
caminho = "NWWWSWWWNEEN"
labirinto.tracePath({agente: caminho}, delay=200)
# dentro do agent podemos passar a linha e coluna que o agente deve começar, filled=true pra prenncher todo o espaço ou não e footprint=true para mostrar o caminho que o agente esta fazendo
# dentro do tracePath indicamos o agente e o caminho criado, além do delay que é o tempo de espera entre um passo e outro
# posicao = agent.position
# print(posicao)

texto = textLabel(labirinto, title="Nº passos", value=len(caminho))

labirinto.run()