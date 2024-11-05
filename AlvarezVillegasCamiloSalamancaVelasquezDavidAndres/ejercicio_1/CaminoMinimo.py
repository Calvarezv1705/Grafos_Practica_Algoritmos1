#la función dijkstra recibe dos parámetros el parametro grafo y el parametro inicio

def dijkstra(grafo, comienzo):

    # crear un diccionario para almacenar las distancias a cada
    # nodo desde el nodo de comienzo
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[comienzo] = 0
    
    # se crea una cola de prioridad para almacenar los nodos a visitar para tratar de simular una heap
    cola = [(0, comienzo)]
    
    #este bucle se ejecutara mientras haya nodos que no se hayan visitados en cola
    while cola:
        #ordena la lista para que el nodo con la menor distancia quede en la primera posición
        cola.sort()
        #elimina y devuelve el primer elemento de la lista
        distanciaActual, nodoActual = cola.pop(0)
        
        # si la distancia actual es mayor que la registrada, continuar
        if distanciaActual > distancias[nodoActual]:
            continue
        
        # aquí se itera sobre todos los vecinos de nodoActual
        for vecino, peso in grafo[nodoActual]:
            distancia = distanciaActual + peso
            
            #si la nueva distancia calculada es menor que la distancia actualmente registrada, entonces se actualiza la distancia y se añade (distancia, vecino) a cola para que el vecino sea procesado en la siguiente iteración
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                cola.append((distancia, vecino))
    
    return distancias

#esta funcion lo que hace es mostrar las conexiones del grafo con su peso para tener una idea de como va este 
def mostrarGrafo(grafo):
    conexiones = set()

    # iterar sobre cada nodo en el grafo
    for nodoInicio, vecinos in grafo.items():
        for nodoFinal, peso in vecinos:
            # crear la representación textual de la conexión
            conexion = f"({nodoInicio}) --{peso}--> ({nodoFinal})"
            
            # imprimir la conexión si no ha sido impresa antes
            if (nodoInicio, nodoFinal) not in conexiones:
                print(conexion)
                
                # registrar la conexión como impresa para evitar duplicados
                conexiones.add((nodoInicio, nodoFinal))

# ejemplo de uso puesto en la guia
grafo = {
    1: [(2, 4), (3, 1)],
    2: [(3, 2), (4, 5)],
    3: [(4, 8)],
    4: []
}

# mostrar el grafo
print("Grafo:")
mostrarGrafo(grafo)

# calcular las distancias usando Dijkstra
comienzo = 1
distancias = dijkstra(grafo, comienzo)

# mostrar las distancias resultantes
print("Distancia mas corta del nodo ", comienzo, "a todos los nodos:")
for nodo, distancia in distancias.items():
    print(f"Distancia a {nodo}: {distancia}")
