
# -*- coding: utf-8 -*-

#from array_queue import ArrayQueue  # array_queue.py eh o nome do arquivo(modulo) e ArrayQueue eh a classe
from array_queue_new import ArrayQueue  # array_queue.py eh o nome do arquivo(modulo) e ArrayQueue eh a classe
from listaSimplesmenteEncadeadaComIteradorFinal_Solucao import ListNode
from listaSimplesmenteEncadeadaComIteradorFinal_Solucao import SinglyLinkedListIterator



if __name__ == "__main__":

    # fila = []
    # fila.append('A')
    # fila.append('B')
    # fila.append('C')
    # // |A|B|C|
    # fila.pop(0)
    #  // |B|C|

    #  // ultimo += 1
    #  // fila[ultimo] = 'H'
    #  // fila[primeiro]
    #  primeiro += 1

    # fila q: [D A B C]
    # fila copia = []

    # concatenar duas filas f1 e f2: adicionar os elementos da fila f2 no final da fila f1
    #                                 restaurar a fila f2

    #def concatFilas(f1, f2):

    #def inesereElemNaPosicaoDada (fila, elem, posicao):

    #fila guarda o peso de cada container
    #retornar True: pestoTotal <= pesoMaximo
    # caso contrario: retornar False
    #def podeDestracar(fila, pesoMaximo):


    #fila q: [A B C]
    #fila copia = []
    #print: [ A B C ]

    # fila q: [A B C]
    # fila copia = []
    # print: [ A B C ]

    def printFila(q): #queue fila
        copia = ArrayQueue()  # instaciou fila auxiliar
        print('[', end="")
        while(not q.is_empty()): # enquanto a fila q nao ficar vazia
            print(q.first(), end=" ") # exibe o elemento que esta como primeiro da fila
            copia.enqueue(q.dequeue()) # adicionar o elem da frente na fila auxiliar e desenfileirar
        while(not copia.is_empty()):
            q.enqueue(copia.dequeue())
        copia = None #ajudar o garbage collector a desalocar
        print(']\n')


    def copiar_fila_original(fila: ArrayQueue):
        copia = ArrayQueue()
        f_restaura = ArrayQueue()
        # percorrer a fila
        while not fila.is_empty():
            #le o elemento
            elem = fila.dequeue()
            #inserir o elemento das duas filas
            copia.enqueue(elem)
            f_restaura.enqueue(elem)

        #restaruar a fila original
        while not f_restaura.is_empty():
            fila.enqueue(f_restaura.dequeue())
        f_restaura = None
        return copia


    def copiar_fila_original_usando_lista(fila: ArrayQueue):
        copia = ArrayQueue()
        lista_apoio = SinglyLinkedListIterator()
        # percorrer a fila original
        while not fila.is_empty():
            #insere na fila copia e na lista
            elem = fila.dequeue()
            copia.enqueue(elem)
            lista_apoio.addNode(elem)

        lista_apoio.first_Node()
        while lista_apoio.iterator:
            fila.enqueue(lista_apoio.iterator.data)
            lista_apoio.elimNode()

        return copia


    def concatFilas(f1, f2):
        copia = copiar_fila_original(f2)
        while not copia.is_empty():
            f1.enqueue(copia.dequeue())


    #Coloca o elemento elem na primeira posição da fila.
    def primeiroDaFila(fila, elem):
        # criar uma fila nova, de apoio
        nova_fila = ArrayQueue()
        # adicionar elem na primeira posicao da nova fila
        nova_fila.enqueue(elem)
        # percorrer a file original, remover os elementos
        # e adicionar no final da nova fila
        while not fila.is_empty():
            nova_fila.enqueue(fila.dequeue())
        # percorrer a nova fila, remover os elementos
        # e adicioanr no final da fila original
        while not nova_fila.is_empty():
            fila.enqueue(nova_fila.dequeue())

    def posicaoDaFila(fila, elem, pos):
        nova_fila = ArrayQueue()
        cont = 1
        while not fila.is_empty():
            if cont == pos:
                nova_fila.enqueue(elem)
            nova_fila.enqueue(fila.dequeue())
            cont += 1
        while not nova_fila.is_empty():
            fila.enqueue(nova_fila.dequeue())

#######################################################
#######################################################
#######################################################

    """1) Fila copiarFila( Fila f ) 
Fazer uma cópia de uma Fila, usando como apoio uma lista. Também é 
possível usar como apoio uma fila. A Fila original deve ser restaurada."""

    def copiarFila(f):
        copia = ArrayQueue() # copia a ser retornada
        copiaRestaura = ArrayQueue() # copia para restaurar a fila f
        while(not f.is_empty()):
            elem = f.dequeue()
            copia.enqueue(elem)
            copiaRestaura.enqueue(elem)
        while(not copiaRestaura.is_empty()):
            f.enqueue(copiaRestaura.dequeue())
        copiaRestaura = None
        return copia



     # f = [ A B C D]  
     # elem = D
     # copia=[A B C D]
     #copiaRestaura=[]


    def copiarFilaUsandoLista(f):
        copia = ArrayQueue() # copia a ser retornada
        lst = SinglyLinkedListIterator() # copia para restaurar a fila f
        while(not f.is_empty()):
            elem = f.dequeue()
            copia.enqueue(elem)
            lst.addNode(elem)
        lst.first_Node() # iterador no primeiro elemento da lista
        while(not iterator):
            f.enqueue(lst.get_iterator().getData()) # lst.iterator.data
            lst.elim_Node()
        lst = None
        return copia

    """3) void concatFilas(Fila f1, Fila f2) 
Concatenar duas filas, deixando o resultado na primeira(f1). A fila f2 deve 
ser restaurada. Sugestão: usar como apoio outra fila."""

    def concatFilas(f1, f2):
        #copia = ArrayQueue() # copia da fila f2 para restauracao
        copia = copiarFila(f2)
        while(not f2.is_empty()): # enquanto a fila f2 nao ficar vazia
            f1.enqueue(f2.dequeue()) # adiciona o primElem de f2 no fim de f1
        while(not copia.is_empty()):
            f2.enqueue(copia.dequeue())
        copia = None

    def concatFilasInteligente(f1, f2):
        copia = copiarFila(f2)
        while(not copia.is_empty()): # enquanto a fila f2 nao ficar vazia
            f1.enqueue(copia.dequeue()) # adiciona o primElem de f2 no fim de f1
        copia = None

    def concatFilasInteligente(f1, f2):
        copia = copiarFila(f2)
        while(not copia.is_empty()):
            f1.enqueue(copia.dequeue())
        copia = None

    def concatFilasInteligente(f1, f2):
        copia = copiarFila(f2)
        while(not copia.is_empty()):
            f1.enqueue(copia.enqueue())
        copia = None

    def concatFilas(f1, f2):
        copia = copiarFila(f2)
        while(not f2.is_empty()):
            f1.dequeue(f2.dequeue())
        while(not copia.is_empty()):
            f2.dequeue(copia.dequeue())
        copia = None

    def concatFilas(f1, f2):
        copia = copiarFila(f2)
        while(not f2.is_empty()):
            f1.enqueue(f2.dequeue())
        while(not copia.is_empty()):
            f2.dequeue(copia.dequeue())
        copia = None

    # def concatFilas(f1, f2):
    #     copia = copiarFila(f2)
    #     while(not f2.is_empty()):
    #         f1.enqueue(f2.dequeue())
    #     while(not copia.is_empty()):
    #         f2.enqueue(copia.enqueue())
    #     copia = None

    #f1=[ A B C E F G]
    #f2=[E F G]
    #quero f1=[A B C E F G]
    #copia=[]

    """10) primeiroDaFila( Fila f, TipoF elem) 
Coloca o elemento elem na primeira posição da fila. """
    def primeiroDaFila(fila, elem):
        filaApoio = ArrayQueue() # crio uma nova fila para guardar
        filaApoio.enqueue(elem) # insiro elem na fila
        while(not fila.is_empty()):
            filaApoio.enqueue(fila.dequeue())
        while(not filaApoio.is_empty()):
            fila.enqueue(filaApoio.dequeue())
        filaApoio = None


    def primeiroDaFila(fila, elem):
        filaApoio = Fila()
        filaApoio.enqueue(elem)
        while (not fila.is_empty()):
            filaApoio.enqueue(fila.enqueue())
        while (not filaApoio.is_empty()):
            fila.enqueue(filaApoio.dequeue())
        filaApoio = None

    def primeiroDaFila(fila, elem):
        filaApoio = Fila()
        filaApoio.enqueue(elem)
        while (not fila.is_empty()):
            filaApoio.dequeue(fila.dequeue())
        while (not filaApoio.is_empty()):
            fila.enqueue(filaApoio.dequeue())
        filaApoio = None

    def primeiroDaFila(fila, elem):
        filaApoio = Fila()
        filaApoio.enqueue(elem)
        while (not fila.is_empty()):
            filaApoio.dequeue(fila.enqueue())
        while (not filaApoio.is_empty()):
            fila.enqueue(filaApoio.dequeue())
        filaApoio = None

    def primeiroDaFila(fila, elem):
        filaApoio = Fila()
        filaApoio.enqueue(elem)
        while (not fila.is_empty()):
            filaApoio.enqueue(fila.dequeue())
        while (not filaApoio.is_empty()):
            fila.dequeue(filaApoio.dequeue())
        filaApoio = None

    def primeiroDaFila(fila, elem):
        filaApoio = Fila()
        filaApoio.enqueue(elem)
        while (not fila.is_empty()):
            filaApoio.enqueue(fila.dequeue())
        while (not filaApoio.is_empty()):
            fila.enqueue(filaApoio.enqueue())
        filaApoio = None


    #supondo que as posicoes da fila: 1 , 2 , 3, ...
    def adicionaNaPosicaoPos_noco(fila, elem, posicao):
        if posicao <= len(fila) and posicao > 0:
             contaPosicao = 1
             filaApoio = ArrayQueue()
             while(not fila.is_empty()):
                 if(contaPosicao == posicao):
                     filaApoio.enqueue(elem)
                     contaPosicao += 1
                 else:
                     filaApoio.enqueue(fila.dequeue())
                     contaPosicao += 1
             while(not filaApoio.is_empty()):
                fila.enqueue(filaApoio.dequeue())
        else:
            print('posicao invalida')


    def elimina_elemento_novo(fila, elem):
        if not fila.is_empty():
            filaApoio = ArrayQueue()
            while not fila.is_empty():
                elem_fila = fila.dequeue()
                if elem_fila != elem:
                    filaApoio.enqueue(elem_fila)
            while not filaApoio.is_empty():
                fila.enqueue(filaApoio.dequeue())



    # adicionar o elmento elem numa posicao pos dada.
    def adicionaNaPosicaoPos(fila, elem, posicao):
        if(len(fila) == 0 and posicao == 0): # filza vazia
            fila.enqueue(elem)
        elif( posicao >=0 and posicao <= len(fila)+1):
            contaPosicao = 0
            filaApoio = ArrayQueue()
            while(not fila.is_empty()):
                if(contaPosicao == posicao): # eh a posicao a ser inserida
                    filaApoio.enqueue(elem)
                    contaPosicao += 1
                else:
                    contaPosicao += 1
                    filaApoio.enqueue(fila.dequeue())
            while(filaApoio):
                fila.enqueue(filaApoio.dequeue())
        else:
            print('posicao invalida')

    """5) int existeElemento( Fila f, TipoF elem) 
Retorna true(1) se o elemento elem está presente na fila e false(0) caso 
contrário. """

    def existeElemento(fila, elem):
        if( fila.is_empty()): # fila vazia
            return False
        else:
            copia = copiarFila(fila)
            while(copia): # enquanto tiver elemento
                if(elem == copia.dequeue()):
                    copia = None # ajudar garbage collector
                    return True
            copia = None
            return False


    def existeElemento(fila, elem):
        if( fila.is_empty()): 
            return False
        else:
            copia = copiarFila(fila)
            while(copia): 
                if(elem != copia.dequeue()):
                    copia = None 
                    return True
            copia = None
            return False

    def podeZapar(cargaMaximaDoNavio, fila):
        carga_containers = 0
        fila_copia = ArrayQueue()
        while not fila.is_empty():
            elem = fila.dequeue()
            carga_containers += elem
            fila_copia.enqueue(elem)
        while not fila_copia.is_empty():
            fila.enqueue(fila_copia.dequeue())
        if carga_containers <= cargaMaximaDoNavio:
            print("Transporte Aprovado")
        else:
            print("Transporte Reprovado")


    def printLista(lista):
        lista.first_Node() # por o iterador sobre o primeiro elemento
        while not lista.isUndefinedIterator():
            print(lista.get_iterator().getData(), end=" ")
            lista.nextNode() # avanca iterador para proximo noh
        print('\n')

    Q = ArrayQueue() # cria uma fila vazia
    Q.enqueue(5) # adiciona no fim da fila o 5
    printFila(Q) # [5 ]
    Q.enqueue(3) # adiciona no fim da fila o 3
    printFila(Q) # [5 3 ]
    print('tamanho da fila = {}'.format(len(Q))) # tamanho da fila = 2
    Q.dequeue() # remove e retorna o primeiro elemento da fila: 5
    printFila(Q) # [3 ]
    if(Q.is_empty()): # verifica se a fila esta vazia
        print('fila vazia')
    else:
        print('fila cheia')
    Q.dequeue() # remove e retorna o primeiro elemento da fila: 3
    printFila(Q)  # [ ]
    if (Q.is_empty()):
        print('fila vazia')
    else:
        print('fila cheia')
    Q.dequeue() # remove e retorna o primeiro elemento da fila: mas já está vazia: fila vazia
    Q.enqueue(7) # [7 ] # adiciona no fim da fila o 7
    printFila(Q)
    Q.enqueue(9)  # [7 9 ] # adiciona no fim da fila o 9
    printFila(Q)  # retorna o primeiro elemento da fila sem remover : 7
    print('primeiro elem da fila = {}'.format(Q.first()))

    fila2 = ArrayQueue() # criando nova fila
    fila2= copiarFila(Q) # criando uma copia da fila Q
    printFila(fila2)
#    concatFilas(fila2,Q)
    printFila((fila2))
    printFila(Q)

#    primeiroDaFila(fila2, 100)
    printFila(fila2)

    adicionaNaPosicaoPos(fila2, 200, 3)
    printFila(fila2)

    if (existeElemento(fila2,200)):
        print('existe 200')
    else:
        print('nao existe 200')

    # for i in range(8):
    #     Q.enqueue(i*10)
    #     print('i={} size={}'.format(i,len(Q)))
    #     printFila(Q)
    #
    # Q.dequeue()
    # Q.enqueue(80)
    # printFila(Q)

    # lst = SinglyLinkedListIterator()
    # for i in range(5):
    #     lst.addNode(i)
    # printLista(lst)


