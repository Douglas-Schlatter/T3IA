import solucao as solucao
import time

complete = "2_3541687"

funcs = [("bfs", solucao.bfs), ("dfs", solucao.dfs), ("hamming", solucao.astar_hamming), ("euclidian", solucao.astar_euclidian), ("manhattan", solucao.astar_manhattan)]

for name, func in funcs:
    print(f"Resultados {name}:")

    start = time.time()

    caminho = func(complete)

    end = time.time() - start

    print(f"{end} seconds")