import networkx as nx 
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

cities = ["Дніпро", "Київ", "Одеса"]
vehicles = ["Нова Пошта", "Делівері", "Intime"]
G.add_nodes_from(cities + vehicles)
initial_edges = [("Дніпро", "Нова Пошта"), ("Київ", "Нова Пошта"), ("Сінгапур", "Делівері"), ("Одеса", "Делівері"), ("Одеса", "Intime")]
G.add_edges_from(initial_edges)

additional_edges = [("Дніпро", "Київ"), ("Київ", "Одеса")]
G.add_edges_from(additional_edges)


pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight="bold", node_size=700, node_color="skyblue", font_color="black", font_size=10, edge_color="gray", connectionstyle="arc3,rad=0.1")
plt.show()


def dfs(graph, start, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    visited.add(start)
    path.append(start)
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, path)
    return path

def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    path = []
    while queue:
        current = queue.pop(0)
        path.append(current)
        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return path

dfs_path = dfs(G, "Дніпро")
bfs_path = bfs(G, "Дніпро")

# Порівняння результатів
print(f"DFS Path: {dfs_path}")
print(f"BFS Path: {bfs_path}")