# Variables
MAX_N = 100010
n = 7  # Ejemplo de un valor para n
a = [2, 8, 5, 3, 7, 9, 1]  # Ejemplo de un arreglo

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

class Node:
    def __init__(self):
        self.sum = 0
        self.mult = 0
        self.min = float('inf')
        self.max = 0
        self.gcd = 0

segmentTree = [Node() for _ in range(2 * MAX_N)]

# Llenar el Segment Tree para luego realizar consultas
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
        # Ir por el lado izquierdo
        init(inicio, mid, nodoIzquierdo)
        # Ir por el lado derecho
        init(mid + 1, final, nodoDerecho)
        segmentTree[nodoActual].sum = segmentTree[nodoIzquierdo].sum + segmentTree[nodoDerecho].sum
        segmentTree[nodoActual].max = max(segmentTree[nodoIzquierdo].max, segmentTree[nodoDerecho].max)
        segmentTree[nodoActual].min = min(segmentTree[nodoIzquierdo].min, segmentTree[nodoDerecho].min)
        segmentTree[nodoActual].gcd = gcd(segmentTree[nodoIzquierdo].gcd, segmentTree[nodoDerecho].gcd)

# Realizar una consulta
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
        result.gcd = gcd(maxIzquierdo.gcd, maxDerecho.gcd)
        return result

# Actualizar un valor en el Segment Tree
def update(inicio, final, nodoActual, posicion, valor):
    if posicion < inicio or posicion > final:
        return

    if inicio == final:
        segmentTree[nodoActual].max = valor
        segmentTree[nodoActual].min = valor
        segmentTree[nodoActual].sum = valor
        segmentTree[nodoActual].gcd = valor
    else:
        mid = (inicio + final) // 2
        nodoIzquierdo = 2 * nodoActual + 1
        nodoDerecho = 2 * nodoActual + 2
        # Actualizar por el lado izquierdo
        update(inicio, mid, nodoIzquierdo, posicion, valor)
        # Actualizar por el lado derecho
        update(mid + 1, final, nodoDerecho, posicion, valor)
        segmentTree[nodoActual].sum = segmentTree[nodoIzquierdo].sum + segmentTree[nodoDerecho].sum
        segmentTree[nodoActual].max = max(segmentTree[nodoIzquierdo].max, segmentTree[nodoDerecho].max)
        segmentTree[nodoActual].min = min(segmentTree[nodoIzquierdo].min, segmentTree[nodoDerecho].min)
        segmentTree[nodoActual].gcd = gcd(segmentTree[nodoIzquierdo].gcd, segmentTree[nodoDerecho].gcd)

# Inicializar el Segment Tree
init(0, n - 1, 0)

for i in range(2 * n):
    print(f"[ {segmentTree[i].sum} ]", end=' ')
print()

queries = 2
for i in range(queries):
    izquierda, derecha = 1, 4
    print(f"El máximo de {izquierda} y {derecha} es: {query(0, n - 1, 0, izquierda, derecha).max}")

# Actualizar un valor en el Segment Tree
update(0, n - 1, 0, 5, 8)
print(f"El máximo de {0} y {6} es: {query(0, n - 1, 0, 0, 6).max}")
