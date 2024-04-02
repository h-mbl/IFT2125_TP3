import sys
from queue import PriorityQueue

global elementVisite
elementVisite = []

def read_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            # Sépare les nombres dans la ligne basée sur la virgule et convertit chaque élément en entier
            row = list(map(int, line.strip().split(',')))
            matrix.append(row)
    # Pas besoin de retourner m et n séparément, car ils peuvent être déduits de la matrice
    return matrix


def add_edge(graph, from_node, to, weight):
    if from_node not in graph:
        graph[from_node] = []
    graph[from_node].append((to, weight))

def build_graph(matrix):
    m, n = len(matrix), len(matrix[0])
    # le graphe est un dictionnaire
    graph = {}
    get_index = lambda row, col: row * n + col

    for i in range(m):
        for j in range(n):
            from_node = get_index(i, j)
            if i > 0:
                add_edge(graph, from_node, get_index(i-1, j), matrix[i-1][j])
            if j > 0:
                add_edge(graph, from_node, get_index(i, j-1), matrix[i][j-1])
            if j < n - 1:
                add_edge(graph, from_node, get_index(i, j+1), matrix[i][j+1])
    return graph

def dijkstra(graph, source, n):
    min_distance = {source: 0}
    pq = PriorityQueue()
    pq.put((0, source))

    while not pq.empty():
        total_weight, node = pq.get()
        if node not in min_distance or total_weight > min_distance[node]:
            continue

        for to, weight in graph.get(node, []):
            new_dist = total_weight + weight
            if to not in min_distance or new_dist < min_distance[to]:
                min_distance[to] = new_dist
                elementVisite.append(to)
                pq.put((new_dist, to))

    min_to_top = sys.maxsize
    for i in range(n):
        min_to_top = min(min_to_top, min_distance.get(i, sys.maxsize))
    return min_to_top

def find_minimum_path(matrix):
    # je suis ici
    graph = build_graph(matrix)
    m, n = len(matrix), len(matrix[0])
    min_path = sys.maxsize
    grandtableau = []
    for i in range(n):
        #elementVisite =[]
        source = (m - 1) * n + i
        min_path = min(min_path, dijkstra(graph, source, n))
        grandtableau.append(min_path)
        print(elementVisite)
        #breakpoint()
    print(grandtableau)
    if 264881 in grandtableau: print("ok")
    return min_path

if __name__ == "__main__":
    filename = "C:/Users/herve/OneDrive/Documents/GitHub/IFT2125_TP3/Q2 Escalade/wall5.txt"
    #filename = "test.txt"
    matrix = read_matrix_from_file(filename)
    min_difficulty = find_minimum_path(matrix)
    print(f"Minimum total difficulty: {min_difficulty}")
