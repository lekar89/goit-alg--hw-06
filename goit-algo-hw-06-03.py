import networkx as nx 
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

cities = ["Дніпро", "Київ", "Одеса"]
vehicles = ["Нова Пошта", "Делівері", "Intime"]
G.add_nodes_from(cities + vehicles)
initial_edges = [("Дніпро", "Нова Пошта",1), ("Київ", "Нова Пошта",2), ("Сінгапур", "Делівері",3), ("Одеса", "Делівері",4), ("Одеса", "Intime"),5]
G.edges_with_weights(initial_edges)


pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, font_weight="bold", node_size=700, node_color="skyblue",
        font_color="black", font_size=10, edge_color="gray", width=2, edge_cmap=plt.cm.Blues)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Мережа  сполучень з вагами")
plt.show()


def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph.nodes()}
    distances[start] = 0

    visited = set()

    while len(visited) < len(graph.nodes()):
        current_node = min(set(distances.keys()) - visited, key=lambda node: distances[node])

        for neighbor, weight in graph[current_node].items():
            if distances[current_node] + weight['weight'] < distances[neighbor]:
                distances[neighbor] = distances[current_node] + weight['weight']

        visited.add(current_node)

    return distances


dijkstra_distances = dijkstra(G, "Дніпро")

# Виведення результатів
print("Dijkstra Distances:")
for node, distance in dijkstra_distances.items():
    print(f"{node}: {distance}")