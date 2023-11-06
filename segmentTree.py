from fontTools.cu2qu.cu2qu import MAX_N


n = 0
a = []
class Node:
    def _init_(self):
        self.sum = 0
        self.max = 0
        self.min = float('inf')


segmentTree = [Node() for _ in range(2 * MAX_N)]

#Se llena el segment tree para luego realizar las consultas
def init(inicio, final, nodoActual):
    if inicio == final:
        segmentTree[nodoActual].max = a[inicio]
        segmentTree[nodoActual].min = a[inicio]
        segmentTree[nodoActual].sum = a[inicio]
    else:
        mid = (inicio + final) // 2
        nodoIzquierdo = 2 * nodoActual + 1
        nodoDerecho = 2 * nodoActual + 2
        init(inicio, mid, nodoIzquierdo)
        init(mid + 1, final, nodoDerecho)
        segmentTree[nodoActual].sum = segmentTree[nodoIzquierdo].sum + segmentTree[nodoDerecho].sum
        segmentTree[nodoActual].max = max(segmentTree[nodoIzquierdo].max, segmentTree[nodoDerecho].max)
        segmentTree[nodoActual].min = min(segmentTree[nodoIzquierdo].min, segmentTree[nodoDerecho].min)

#Aqui se realiza la consulta de los resultados
def query(inicio, final, nodoActual, izquierda, derecha):
    if inicio >= izquierda and final <= derecha:
        return segmentTree[nodoActual]

    mid = (inicio + final) // 2
    nodoIzquierdo = 2 * nodoActual + 1
    nodoDerecho = 2 * nodoActual + 2

    if derecha <= mid:
        return query(inicio, mid, nodoIzquierdo, izquierda, derecha)
    elif izquierda > mid:
        return query(mid + 1, final, nodoDerecho, izquierda, derecha)
    else:
        maxIzquierdo = query(inicio, mid, nodoIzquierdo, izquierda, derecha)
        maxDerecho = query(mid + 1, final, nodoDerecho, izquierda, derecha)
        result = Node()
        result.sum = maxIzquierdo.sum + maxDerecho.sum
        result.max = max(maxIzquierdo.max, maxDerecho.max)
        result.min = min(maxIzquierdo.min, maxDerecho.min)
        return result


# # Ejemplo de uso:
# n = 6
# a = [4, 2, 1, 6, 8, 5]
#
# init(0, n - 1, 0)
# resultado = query(0, n - 1, 0, 2, 4)
# print("Suma:", resultado.sum)
# print("Máximo:", resultado.max)
# print("Mínimo:", resultado.min)
# print("GCD:", resultado.gcd)
