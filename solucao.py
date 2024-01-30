from typing import Iterable, Set, Tuple

class Nodo:


    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, acao:str, custo:int): #-> deixamos comentado aqui por enquanto para conseguir testar a ex1
    #def __init__(self, estado:str, pai, acao:str, custo:int):

        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        # substitua a linha abaixo pelo seu codigo
        self.estado = estado
        self.pai= None
        self.acao = acao
        self.custo = custo + 1
        #raise NotImplementedError

def addFather(child: Nodo , pai:Nodo):
    child.pai = pai


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
    raise NotImplementedError


def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


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
    raise NotImplementedError

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
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

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
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

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
