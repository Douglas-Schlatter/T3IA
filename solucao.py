from typing import Iterable, Set, Tuple
import queue
from collections import deque

class Nodo:

    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai: 'Nodo', acao:str, custo:int):

        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        # substitua a linha abaixo pelo seu codigo
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
        self.custaGeral =None
    
    def __lt__(self, other):
        return self.custaGeral < other.custaGeral

    # def setCustoGeral(self,custoH : int):
    #     self.custoGeral = self.custo +custoH


def trocaChar(estado, pos, pos2):
    #print("estado recebido: "+ estado)
    iCarac = estado[pos]
    newEst = estado
    newEst = newEst[:pos] +'_'+ newEst[pos+1:]
    newEst = newEst[:pos2] + iCarac + newEst[pos2+1:]
    #print("estado: " + newEst)
    return newEst


def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
     # substituir a linha abaixo pelo seu codigo
   # raise NotImplementedError
    cTuplas = set()
    #cTuplas = []
    blankPos = estado.rfind('_')

# string = string[:position] + new_character + string[position+1:]
    if (blankPos >= 3):    
       # cTuplas.add(("acima",newEst))
        #cTuplas.add(("acima",trocaChar(estado, blankPos-3, blankPos)))
        cTuplas.add(("acima",trocaChar(estado, blankPos-3, blankPos)))
        # pode ir pra cima
        #   trocar barra com barra-3 
    if (blankPos <= 5):
       # """
        #cTuplas.add(0)
        #print("estado recebido: "+ estado)
        #iCarac = estado[blankPos+3]
        #newEst = estado 
        #newEst = newEst[:blankPos+3] +'_'+ newEst[blankPos+4:]
        #newEst = newEst[:blankPos] + iCarac + newEst[blankPos+1:]
        #print("tupla de saida: " + "(abaixo,"+ newEst+")")
        #cTuplas.add(("abaixo",newEst))
        #"""
        cTuplas.add(("abaixo",trocaChar(estado, blankPos+3, blankPos)))
        # pode ir pra baixo
        #   trocar barra com barra+3

    if (blankPos % 3 != 0):
        # pode ir para a esquerda
        #   trocar barra com barra -1
        cTuplas.add(("esquerda",trocaChar(estado, blankPos-1, blankPos)))

    if (blankPos % 3 != 2):
        # pode ir para a direita
        #   trocar barra com barra +1
        cTuplas.add(("direita",trocaChar(estado, blankPos+1, blankPos)))
        #print("tupla final " + str(cTuplas))
        #print("Quantos sucessores? " + str(len(cTuplas)))
    return cTuplas
    """
    if(4 ==estado.rfind('_')):
        print("aqui esta no super meio")
        
        #aqui esta no super meio

        return 0
    elif (estado.rfind('_')%2 == 0):
        print("Esta em uma das pontas")
        #Esta em uma das pontas
        return 0
    else:
        print("Esta em um dos meios")
        #Esta em um dos meios
        return 0
     """
   


def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    listaNodos = set()
    for acao, estado in sucessor(nodo.estado):
        listaNodos.add(Nodo(estado, nodo, acao, nodo.custo+1))
    return listaNodos

def caminho(nodo: Nodo):

    caminho = []
    nodoAtual = nodo

    while(nodoAtual.pai != None):
        caminho.append(nodoAtual.acao)
        nodoAtual = nodoAtual.pai
    caminho.reverse()            #Precisa inverter porque é adicionado o caminho ao contrario na lista
    return caminho

def get_inv_count(arr):
    inv_count = 0
    for i in range(8):  
        for j in range(i + 1, 9):
            if arr[i] != '_' and arr[j] != '_' and arr[i] > arr[j]:
                inv_count += 1
    return inv_count

def is_solvable(puzzle_str):
    puzzle_list = list(puzzle_str)
    inv_count = get_inv_count(puzzle_list)
    return inv_count % 2 == 0

def astar_geral(heu: str, estado: str):

    if not is_solvable(estado):
        return None

    func = 0
    expansoes = 0
    if heu=='h':
        func=numHamming
    elif heu=='m':
        func=numManhattan
    elif heu =='e':
        func=numEuclidian 

    visitados = []
    #fronteira = [Nodo(estado, None, '', 0)]
    fronteira = queue.PriorityQueue()
    first_node = Nodo(estado, None, '', 0)
    first_node.custaGeral = func(first_node.estado)
    fronteira.put(first_node)

    while not fronteira.empty():
        nodoAtual = fronteira.get()
        if (nodoAtual.estado == "12345678_"):
            print(f"Custo final {nodoAtual.custo}")
            print(f"Número de expansões {expansoes}")
            return caminho(nodoAtual)
        elif(nodoAtual.estado not in visitados):# nodo atual ja esta em visitados? Se não adicione o a visitados e verifique seus visinhos
            visitados.append(nodoAtual.estado)
            expansoes+=1
            for iNodo in expande(nodoAtual):
                if (iNodo.estado not in visitados):
                    iNodo.custaGeral = iNodo.custo + func(iNodo.estado)
                    fronteira.put(iNodo)

    return None

def numHamming(estado: str): #Calcula quantos quadrados estão fora do lugar
    valorHam = 0
    for pos, letra in enumerate(estado):
        if (letra == '_'):
            if (pos != 8):
                valorHam += 1
        elif (int(letra) != pos+1):
            valorHam += 1
    return valorHam

def numManhattan(estado: str):
    obj = "12345678_"
    estado = list(estado)
    manhattan = 0
    for i in range(9):
        if(estado[i] != obj[i]):
            pos_atual = estado.index(estado[i])
            pos_obj = obj.index(estado[i])
            dist_x = abs(pos_atual % 3 - pos_obj % 3)
            dist_y = abs(pos_atual // 3 - pos_obj // 3)
            manhattan += dist_x + dist_y
    return manhattan


def numEuclidian(estado: str):
    obj = "12345678_"
    estado = list(estado)
    euclidian_dist = 0
    for i in range(9):
        if(estado[i] != obj[i]):
            pos_atual = estado.index(estado[i])
            pos_obj = obj.index(estado[i])
            dist_x = abs(pos_atual % 3 - pos_obj % 3)
            dist_y = abs(pos_atual // 3 - pos_obj // 3)
            euclidian_dist += (dist_x**2 + dist_y**2) ** 0.5
    return euclidian_dist

def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """


    return astar_geral('h',estado)
            

def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    return astar_geral('m',estado)

def astar_euclidian(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias Euclidianas e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    return astar_geral('e',estado)

#opcional,extra
def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    if not is_solvable(estado):
        return None

    expansoes = 0
    visitados = set()

    first_node = Nodo(estado, None, '', 0)
    fronteira = deque([first_node])

    while fronteira:
        nodoAtual = fronteira.popleft()
        if (nodoAtual.estado == "12345678_"):
            print(f"Custo final {nodoAtual.custo}")
            print(f"Número de expansões {expansoes}")
            return caminho(nodoAtual)
        elif(nodoAtual.estado not in visitados):# nodo atual ja esta em visitados? Se não adicione o a visitados e verifique seus visinhos
            visitados.add(nodoAtual.estado)
            expansoes+=1
            for iNodo in expande(nodoAtual):
                if (iNodo.estado not in visitados):
                    fronteira.append(iNodo)

    return None

#opcional,extra
def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    if not is_solvable(estado):
        return None

    expansoes = 0
    visitados = set()

    first_node = Nodo(estado, None, '', 0)
    fronteira = [first_node]

    while fronteira:
        nodoAtual = fronteira.pop()
        if (nodoAtual.estado == "12345678_"):
            print(f"Custo final {nodoAtual.custo}")
            print(f"Número de expansões {expansoes}")
            return caminho(nodoAtual)
        elif(nodoAtual.estado not in visitados):# nodo atual ja esta em visitados? Se não adicione o a visitados e verifique seus visinhos
            visitados.add(nodoAtual.estado)
            expansoes+=1
            for iNodo in expande(nodoAtual):
                if (iNodo.estado not in visitados):
                    fronteira.append(iNodo)

    return None

#opcional,extra
def astar_new_heuristic(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError