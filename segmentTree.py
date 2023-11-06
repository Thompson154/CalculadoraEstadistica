MAX_N = 100010

class Node:
    def __init__(self):
        self.sum = 0
        self.min = 0
        self.max = 0
        self.promedio = 0

a = [0]*MAX_N
segmentTree = [Node() for _ in range(MAX_N*2)]

def init(inicio, final, nodoActual):
    if inicio == final:
        segmentTree[nodoActual].max = a[inicio]
        segmentTree[nodoActual].min = a[inicio]
        segmentTree[nodoActual].sum = a[inicio]
        segmentTree[nodoActual].promedio = a[inicio]
    else:
        mid = (inicio + final) // 2
        nodoIzquierdo = 2 * nodoActual + 1
        nodoDerecho = 2 * nodoActual + 2
        init(inicio, mid, nodoIzquierdo)
        init(mid+1, final, nodoDerecho)
        segmentTree[nodoActual].sum = segmentTree[nodoIzquierdo].sum + segmentTree[nodoDerecho].sum
        segmentTree[nodoActual].max = max(segmentTree[nodoIzquierdo].max, segmentTree[nodoDerecho].max)
        segmentTree[nodoActual].min = min(segmentTree[nodoIzquierdo].min, segmentTree[nodoDerecho].min)
        segmentTree[nodoActual].promedio = (segmentTree[nodoIzquierdo].sum + segmentTree[nodoDerecho].sum)/(nodoDerecho-nodoActual)

def query(inicio, final, nodoActual, izquierda, derecha):
    if inicio >= izquierda and final <= derecha:
        return segmentTree[nodoActual]
    mid = (inicio + final) // 2
    nodoIzquierdo = 2 * nodoActual + 1
    nodoDerecho = 2 * nodoActual + 2
    if derecha <= mid:
        return query(inicio, mid, nodoIzquierdo, izquierda, derecha)
    elif izquierda > mid:
        return query(mid+1, final, nodoDerecho, izquierda, derecha)
    else:
        maxIzquierdo = query(inicio, mid, nodoIzquierdo, izquierda, derecha)
        maxDerecho = query(mid+1, final, nodoDerecho, izquierda, derecha)
        result = Node()
        result.sum = maxIzquierdo.sum + maxDerecho.sum
        result.max = max(maxIzquierdo.max, maxDerecho.max)
        result.min = min(maxIzquierdo.min, maxDerecho.min)
        result.promedio = (maxIzquierdo.sum + maxDerecho.sum)/(derecha-izquierda)
        return result

