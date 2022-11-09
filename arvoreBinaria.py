# -*- coding: utf-8 -*-

class NodeABB:

    def __init__(self, data=None, esq=None, dir=None):
      self._data = data
      self._esq = esq
      self._dir = dir
      if self._data:
          self._size = 1
      else:
          self._size = 0

    def setRaizArbin(self, elem):
        self._data = elem

    def raizArbin(self):
        return self._data

    def setDirArbin(self, arbin):
        self._dir = arbin

    def dirArbin(self):
        return self._dir

    def setEsqArbin(self, arbin):
        self._esq = arbin

    def esqArbin(self):
        return self._esq

    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    # def vaziaArbin(self): # basta verificar se a instancia eh Nulo: None

    def add(self, node): # caso da Arv vazia esta sendo tratada no construtor
        if node._data < self._data: # data < raiz : inserir na subArvore esquerda
            if self._esq is None: # subArvEsq eh vazia
                self._esq = node
            else:
                self._esq.add(node)
        elif node._data > self._data: # data > raiz : inserir na subArv direita
            if self._dir is None:
                self._dir = node
            else:
                self._dir.add(node)
        self._size += 1


    def min(self):
        """Retorna o menor elemento da subárvore que tem self como raiz.
        """
        if self._esq is None:
            return self
        else:
            return self._esq.min()

    def removeMin(self):
        """Remove o menor elemento da subárvore que tem self como raiz.
        """
        if self._esq is None:  # encontrou o min, daí pode rearranjar
            return self._dir
        self._esq = self._esq.removeMin()
        return self

    def remove(self, elem):
        if elem < self._data:
            self._esq = self._esq.remove(elem)
        elif elem > self._data:
            self._dir = self._dir.remove(elem)
        else:
            # encontramos o elemento, então vamos removê-lo!
            if self._dir is None:
                return self._esq
            if self._esq is None:
                return self._dir
            # ao invés de remover o nó, copiamos os valores do nó substituto
            tmp = self._dir.min()
            self._data = tmp._data
            self._dir.removeMin()
        return self

if __name__ == '__main__':


    def preOrdemArbin(node:NodeABB):
        if node is not None:#if not node.vaziaArbin():
            print(node._data)
            if node._esq is not None:
                preOrdemArbin(node._esq)
            if node._dir is not None:
                preOrdemArbin(node._dir)

    def preOrdemArbin2(node:NodeABB):
        if node is not None:
            print(node._data)
            if node.esqArbin() is not None: 
                preOrdemArbin(node.esqArbin())
            if node.dirArbin() is not None:
                preOrdemArbin(node.dirArbin())


    # -------------------------------------------------------------------------------
    # Exercícios de Arvore Binaria : pode ter elementos repetidos e não segue uma ordenação
    #  -------------------------------------------------------------------------------

    """1) int pesoArbin( Arbin a){...} 
    Calcular e retornar o peso de uma árvore binária ( número de elementos da árvore). 
    Obs: a complexidade desta função é O(N) 
    """

    def pesoArbin(arbin:NodeABB):
        # se a arbin esta vazia retornar zero
        # senao tem pelo menos uma raiz:
        # retornar 1 + peso da subArv esq + peso subArvDir
        if not arbin: # arvore vazia
            return 0
        else:
            return ( 1 + pesoArbin(arbin._esq) + pesoArbin(arbin._dir))
       


    """2) int estaArbin( Arbin a, TipoA elem){...} 
    Verificar se um elemento está presente em uma árvore binária. 
    Obs: a complexidade desta função é O(N) se a árvore estiver degenerada e O(log N) se a 
    árvore estiver balanceada(cheia).
    """
    def estaArbin(arbin:NodeABB, elem):
        # se arbin vazia entao elem nao esta: retornar False
        # se elem == raiz, elem esta presente: retornar True
        # do contrario procurar elem na subArv esq e dir

        # se arbin vazia entao elem nao esta: retornar False
        if(not arbin):
            return False
        # se elem == raiz, ou seja arbin._data == elem, elem esta presente: retornar True
        elif(arbin._data == elem):
            return True
        # else: retornar estaArbin passando como argumento a subarvore esqquerda or com subarv direita
        else:
            return estaArbin(arbin._esq, elem) or estaArbin(arbin._dir, elem)

        

    """3) int numFolhas( Arbin a){...}  
    Calcular o número de folhas de uma Arbin. 
    Obs: a complexidade desta função é O(N) 
    """
    def numFolhas(arbin:NodeABB):
        # se arbin vazia nao tem folhas: retornar zero
        if arbin is None:
            return 0
        # se tem uma raiz com as duas subArv esq e dir vazias entao tem 1 folha
        # retornar  1
        elif arbin._esq == None and arbin._dir == None: # OU elif arbin.esqArbin() and arbin.dirArbin()
            return 1
        # senao procurar pela folhas na subArv Esq e Dir
        else:
            return numFolhas(arbin._esq) + numFolhas(arbin._dir)

        

    """4) int numOcorrencias( Arbin a){...}  
    Calcular o número de vezes que um elemento aparece na Arbin. 
    Obs: a complexidade desta função é O(N)
    """
    def numOcorrencias( arbin: NodeABB, elem ):
        return 0


    # -------------------------------------------------------------------------------
    # Exercícios de ABB (Arvore Binaria de Busca) ou ABP (Arv. Binaria de Pesquisa)
    # Não pode ter elementos repetidos e segue uma ordem
    #  -------------------------------------------------------------------------------

    # verifica se o elem esta presente na ABB arbin
    def estaArbinBusca(arbin:NodeABB, elem):
        if (arbin is None):  # arv vazia: elem nao esta presente
            return False
        elif (arbin.raizArbin() == elem):  # elem esta presente
            return True
        elif (elem < arbin.raizArbin()):  # procurar elem na subArv Esquerda
            return (estaArbinBusca(arbin.esqArbin(), elem))
        else:  # elem > raizArbin : procurar elem na subArv Direita
            return (estaArbinBusca(arbin.dirArbin(), elem))


    # verifica se o elem esta presente na ABB arbin
    def insArbinBusca2( arbin:NodeABB, elem):
        #arbin vazia: chama o construtor
        if arbin is None:
            arbin = NodeABB(elem)
        elif elem < arbin.raizArbin():  #arbin._data
            arbin._esq = insArbinBusca2(arbin._esq, elem)
        elif elem > arbin.raizArbin():  #arbin._data
            arbin._dir = insArbinBusca2(arbin._dir, elem)
        return arbin

       
    #arbin = insArbinBusca2(arbin, 31)

    def insArbinBusca( arbin:NodeABB, elem):
        #arbin vazia: chama o construtor
        return 0
        


    def maiorElemento(arbin:NodeABB):
        if arbin and arbin.dirArbin() is None:
            return arbin.raizArbin()
        else:
            return maiorElemento(arbin.dirArbin())



    def elimArbinBusca(arbin:NodeABB, elem):
        #arbinAux = None
        #maior = None
        if(arbin.raizArbin() == elem):
            if(arbin.esqArbin() is None and arbin.dirArbin() is None):
                arbin = None
                return None
            elif (arbin.esqArbin() is None):
                arbinAux = arbin.dirArbin()
                arbin = None
                return arbinAux
            else:
                maior = maiorElemento(arbin.esqArbin())
                #print('maior = {}'.format(maior))
                #arbin._data = maior
                #arbin._esq = elimArbinBusca(arbin.esqArbin(), maior)
                arbin.setRaizArbin(maior)
                arbin.setEsqArbin(elimArbinBusca(arbin.esqArbin(), maior))
        elif (elem < arbin.raizArbin()):
            arbin.setEsqArbin(elimArbinBusca(arbin.esqArbin(),elem))
            #arbin._esq = elimArbinBusca(arbin.esqArbin(), elem)
        else:
            arbin.setDirArbin(elimArbinBusca(arbin.dirArbin(),elem))
            #arbin._dir = elimArbinBusca(arbin.dirArbin(), elem)
        return arbin

    def altura_arbin(arbin:NodeABB):
        return 0
        

    def nivel_elem(arbin:NodeABB , elem):
        return 0
        






    #---------------------------------------------------------------------
    # chamada dos metodos implementados
    #---------------------------------------------------------------------
    node = NodeABB(50)
    print("Peso ou qtde elem = {}".format(pesoArbin(node)))
    print('numFolhas = {}'.format(numFolhas(node)))
    node2 = NodeABB(40)
    node3 = NodeABB(60)
    #print(node._data)
    #preOrdemArbin2(node)
    node.add(node2) # node com 50 vai ser a raiz da arvore
    print("Peso ou qtde elem = {}".format(pesoArbin(node)))
    print('numFolhas = {}'.format(numFolhas(node)))
    #preOrdemArbin2(node)
    node.add(node3)
    print("Peso ou qtde elem = {}".format(pesoArbin(node)))
    print('numFolhas = {}'.format(numFolhas(node)))

    print('numOcorrencias 50 = {}'.format(numOcorrencias(node,50)))
    print('numOcorrencias 80 = {}'.format(numOcorrencias(node,80)))

    print('altura = {}'.format(altura_arbin(node)))
    print('nivel 60 = {}'.format(nivel_elem(node, 60)))

    preOrdemArbin2(node)

    if (estaArbin(node,60)):
        print('60 esta na arbin')
    else:
        print('60 nao esta na arbin')

    if (estaArbin(node, 80)):
        print('80 esta na arbin')
    else:
        print('80 nao esta na arbin')
    # pesoArbin
    # print("Peso ou qtde elem = {}".format(pesoArbin(node)))

    # Arbin Busca ABB
    if estaArbinBusca(node, 40):
        print('40 esta na ABB')
    else:
        print('40 nao esta na ABB')

    if estaArbinBusca(node, 100):
        print('100 esta na ABB')
    else:
        print('100 nao esta na ABB')

    print("/n ============================================ /n")

    aBB = None # aBB arvore vazia
    aBB = insArbinBusca2(aBB, 100) # raiz da arvore: 100
    #preOrdemArbin2(aBB)
    aBB = insArbinBusca2(aBB, 45)
    aBB = insArbinBusca2(aBB, 200)
    aBB = insArbinBusca2(aBB, 300)
    aBB = insArbinBusca2(aBB, 250)

    print('###### imprimindo a arvore em pre-ordem  ######')
    preOrdemArbin2(aBB)
    print('############################################################')
    print(f'numero de folhas de aBB = {numFolhas(aBB)}')

    print('###### Maior elemento  ######')
    #print('maior = {}'.format(maiorElemento(aBB)))
    print('###### Eliminando elem 200  ######')
    #aBB = elimArbinBusca(aBB, 200)
    #preOrdemArbin2(aBB)

    print("/n ============================================ /n")
    print('numero de folhas = ', numFolhas(aBB))
    # aBB = aBB.remove(200)
    # preOrdemArbin2(aBB)

    #       100
    #    45     200
    #              300
    #            250


    #numFolhas(vazia)
    #numFolhas(250)
    #numFolhas(300):numFolhas(250) + numFolhas(vazia): 1 + 0
    #numFolhas(vazia)
    #numFolhas(200):numFolhas(vazia) + numFolhas(300) = 0 + 1
    #numFolhas(45)
    #numFolhas(100) : numFolhas(45) + numFolhas(200) = 1 + 1 = 2

    