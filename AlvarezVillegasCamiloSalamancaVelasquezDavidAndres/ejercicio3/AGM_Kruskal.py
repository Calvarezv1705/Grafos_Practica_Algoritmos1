#La función find busca el padre de un nodo si el nodo no es su propio padre, sigue buscando hasta encontrar la raíz del árbol.
def find(padre, i):
    if padre[i] == i:
        return i
    return find(padre, padre[i])

#La función union une dos subconjuntos en un solo conjunto, si los subconjuntos son diferentes, se unen y se actualiza el rango de la raíz del árbol.
def union(padre, rango, x, y):
    raizX = find(padre, x)
    raizY = find(padre, y)

    if raizX != raizY:
        if rango[raizX] > rango[raizY]:
            padre[raizY] = raizX
        elif rango[raizX] < rango[raizY]:
            padre[raizX] = raizY
        else:
            padre[raizY] = raizX
            rango[raizX] += 1

#La función kruskal implementa el algoritmo de Kruskal para encontrar el árbol de expansión mínima de un grafo.
def kruskal(grafo):
    # se ordenan las aristas por peso ascendente para las conexiones más baratas
    grafo.sort(key=lambda x: x[2])
    #se obtiene el número total de nodos en el grafo
    n = max(max(u, v) for u, v, _ in grafo) + 1
    padre = list(range(n))
    rango = [0] * n
    agm = []

    # se recorren las aristas del grafo
    for u, v, peso in grafo:
        if find(padre, u) != find(padre, v):
            union(padre, rango, u, v)
            agm.append((u, v, peso))

    return agm

# Ejemplo de uso de la guia 
grafo = [
    (1, 2, 4),
    (1, 3, 3),
    (2, 4, 2),
    (3, 4, 5)
]
agm = kruskal(grafo)
print(agm)