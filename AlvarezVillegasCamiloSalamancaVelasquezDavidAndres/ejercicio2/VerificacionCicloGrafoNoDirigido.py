#esta es la función principal que verifica si hay un ciclo en el grafo esta usa otra función llamada dfs y un conjunto visitados
def contiene_ciclo(grafo):
    #la función dfs recibe un nodo y su padre, y explora todos los nodos vecinos de ese nodo si encuentra un nodo visitado y que no es el padre, entonces hay un ciclo 
    def dfs(v, padre):
        visitado.add(v)
        # esta devuelve True si encuentra un ciclo y False en caso contrario.
        for vecino in grafo[v]:
            if vecino not in visitado:
                if dfs(vecino, v):
                    return True
                #la siguiente linea evita que hayan falsos positivos en el caso de que el vecino sea el padre
            elif vecino != padre:
                return True
        return False
    #creamos un conjunto para llevar un registro de los nodos visitados
    visitado = set()
    for nodo in grafo:
        if nodo not in visitado:
            if dfs(nodo, None):
                return True
    return False

# ejemplo de uso de la guia
grafo = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}
print(contiene_ciclo(grafo))