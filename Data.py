import segmentTree


def hola():
    n = 10
    a = [1, 5, 20, 5, 5, 6, 7, 8, 9, 10]

    segmentTree.init(0, n - 1, 0)
    result = segmentTree.query(0, n - 1, 0, 1, 5)
    print(f"Max: {result.max}, Min: {result.min}, GCD: {result.gcd}")

    segmentTree.update(0, n - 1, 0, 2, 100)
    result = segmentTree.query(0, n - 1, 0, 1, 5)
    print(f"Max: {result.max}, Min: {result.min}, GCD: {result.gcd}")

hola()