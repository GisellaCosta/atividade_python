from array_queue_new import ArrayQueue
from arvoreBinaria import NodeABB


def iguaisArbin(arbin1: NodeABB, arbin2: NodeABB):
    if arbin1 is None and arbin2 is None:
        return True

    if (arbin1 is not None and arbin2 is not None) and (arbin1._data == arbin2._data):
        return iguaisArbin(arbin1.esqArbin(), arbin2.esqArbin()) and iguaisArbin(arbin2.dirArbin(), arbin2.dirArbin())
    else:
        return False


def nivelArbin(arbin: NodeABB):
    if arbin is None:
        print("\n Árvore vazia.")

    fila = ArrayQueue()
    fila.enqueue(arbin)

    while not fila.is_empty():
        arbin = fila.dequeue()
        if arbin.esqArbin() is not None:
            fila.enqueue(arbin.esqArbin())

        if arbin.dirArbin() is not None:
            fila.enqueue(arbin.dirArbin())

        print(arbin._data, end=" ")


def menorElemento(arbin: NodeABB):
    if arbin is None:
        print("\n Árvore vazia.")

    if arbin.esqArbin() is None:
        return arbin._data
    else:
        return menorElemento(arbin.esqArbin())

def maiorElemento(arbin:NodeABB):
    if arbin is None:
        print("\n Árvore vazia.")

    if arbin.dirArbin() is None:
        return arbin._data
    else:
        return maiorElemento(arbin.dirArbin())


if __name__ == '__main__':
    arbin1 = NodeABB(80)
    node2 = NodeABB(10)
    node3 = NodeABB(30)
    node4 = NodeABB(50)
    node5 = NodeABB(20)
    node6 = NodeABB(55)

    arbin1.add(node2)
    arbin1.add(node3)
    arbin1.add(node4)
    arbin1.add(node5)
    arbin1.add(node6)

    arbin2 = NodeABB(10)
    no2 = NodeABB(80)
    no3 = NodeABB(90)
    no4 = NodeABB(60)
    no5 = NodeABB(30)
    no6 = NodeABB(55)
    arbin2.add(no2)
    arbin2.add(no3)
    arbin2.add(no4)
    arbin2.add(no5)
    arbin2.add(no6)

    if iguaisArbin(arbin1, arbin2):
        print("As árvores binárias são iguais!")
    else:
        print("As árvores binárias não são iguais!")

    nivelArbin(arbin1)

    print(f"\nMenor : {menorElemento(arbin1)}")
    print(f"Maior : {maiorElemento(arbin1)}")