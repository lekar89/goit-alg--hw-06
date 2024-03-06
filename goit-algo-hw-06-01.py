import networkx as nx
import matplotlib.pyplot as plt

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

# Аналіз основних характеристик
print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")
print(f"Ступінь вершин: {dict(G.degree())}")