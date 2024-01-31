import unittest
import timer
import solucao as solucao


class TestaSolucao(unittest.TestCase):
    
    def test_funcao_sucessor(self):
        """
        Testa a funcao sucessor para o estado "2_3541687"
        :return:

        """
        # a lista de sucessores esperados é igual ao conjunto abaixo (ordem nao importa)
        succ_esperados = {("abaixo", "2435_1687"), ("esquerda", "_23541687"), ("direita", "23_541687")}

        sucessores = solucao.sucessor("2_3541687")  # obtem os sucessores chamando a funcao implementada
        self.assertEqual(3, len(sucessores))     # verifica se foram retornados 3 sucessores
        for s in sucessores:                     # verifica se os sucessores retornados estao entre os esperados
            self.assertIn(s, succ_esperados)

    def test_funcao_expande(self):
        """
        Testa a função expande para um Node com estado "185432_67" e custo 2
        :return:
        """
        estado_pai = "185432_67"
        pai = solucao.Nodo(estado_pai, None, "abaixo", 2)  # o pai do pai esta incorreto, mas nao interfere no teste
        # a resposta esperada deve conter nodos com os seguintes atributos (ordem dos nodos nao importa)
        resposta_esperada = {
            ("185_32467", estado_pai, "acima", 3),
            ("1854326_7", estado_pai, "direita", 3),
        }

        resposta = solucao.expande(pai)  # obtem a resposta chamando a funcao implementada
        self.assertEqual(2, len(resposta))  # verifica se foram retornados 2 nodos
        for nodo in resposta:
            # verifica se a tupla com os atributos do nodo esta' presente no conjunto com os nodos esperados
            self.assertIn((nodo.estado, nodo.pai.estado, nodo.acao, nodo.custo), resposta_esperada)

    def run_algorithm(self, alg, input):
        """
        Um helper que executa o algoritmo verificando timeout. Falha se der timeout
        ou retorna a resposta do algoritmo caso contrario.
        """
        response = timer.timeout(
            alg,
            args=(input,),  # must be a 1-element tuple or it doesn't work
            time_limit=60, default='timeout'
        )
        if response == 'timeout':
            self.fail(f"{alg.__name__}: timeout")

        return response

   
  

if __name__ == '__main__':
    unittest.main()
