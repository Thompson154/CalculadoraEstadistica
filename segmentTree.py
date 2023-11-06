MAX_N = 100010

class Node:
    def __init__(self):
        self.sum = 0
        self.min = 0
        self.max = 0
        self.gcd = 0

a = [0]*MAX_N
segmentTree = [Node() for _ in range(MAX_N*2)]

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def init(inicio, final, nodoActual):
    if inicio == final:
        segmentTree[nodoActual].max = a[inicio]
        segmentTree[nodoActual].min = a[inicio]
        segmentTree[nodoActual].sum = a[inicio]
        segmentTree[nodoActual].gcd = a[inicio]
    else:
        mid = (inicio + final) // 2
        nodoIzquierdo = 2 * nodoActual + 1
        nodoDerecho = 2 * nodoActual + 2
        init(inicio, mid, nodoIzquierdo)
        init(mid+1, final, nodoDerecho)
        segmentTree[nodoActual].sum = segmentTree[nodoIzquierdo].sum + segmentTree[nodoDerecho].sum
        segmentTree[nodoActual].max = max(segmentTree[nodoIzquierdo].max, segmentTree[nodoDerecho].max)
        segmentTree[nodoActual].min = min(segmentTree[nodoIzquierdo].min, segmentTree[nodoDerecho].min)
        segmentTree[nodoActual].gcd = gcd(segmentTree[nodoIzquierdo].gcd, segmentTree[nodoDerecho].gcd)

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
        result.max = max(maxIzquierdo.max, maxDerecho.max)
        result.min = min(maxIzquierdo.min, maxDerecho.min)
        result.gcd = gcd(maxIzquierdo.gcd, maxDerecho.gcd)
        result.sum = maxIzquierdo.sum + maxDerecho.sum  # Agregamos la suma aquí
        return result

# def update(inicio, final, nodoActual, posicion, valor):
#     if posicion < inicio or posicion > final:
#         return
#     if inicio == final:
#         segmentTree[nodoActual].max = valor
#         segmentTree[nodoActual].min = valor
#         segmentTree[nodoActual].sum = valor
#     else:
#         mid = (inicio + final) // 2
#         nodoIzquierdo = 2 * nodoActual + 1
#         nodoDerecho = 2 * nodoActual + 2
#         update(inicio, mid, nodoIzquierdo, posicion, valor)
#         update(mid+1, final, nodoDerecho, posicion, valor)
#         segmentTree[nodoActual].sum = segmentTree[nodoIzquierdo].sum + segmentTree[nodoDerecho].sum
#         segmentTree[nodoActual].max = max(segmentTree[nodoIzquierdo].max, segmentTree[nodoDerecho].max)
#         segmentTree[nodoActual].min = min(segmentTree[nodoIzquierdo].min, segmentTree[nodoDerecho].min)

