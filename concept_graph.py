import networkx as nx
import matplotlib.pyplot as plt


def draw_conceptual_graph():
    G = nx.Graph()
    movies = ['Movie A', 'Movie B', 'Movie C']
    casts = ['Cast 1', 'Cast 2', 'Cast 3', 'Cast 4']

    G.add_nodes_from(movies, bipartite=0, type='movie')
    G.add_nodes_from(casts, bipartite=1, type='cast')

    edges = [('Movie A', 'Cast 1'), ('Movie A', 'Cast 2'), ('Movie B', 'Cast 3'), ('Movie C', 'Cast 2'),
             ('Movie C', 'Cast 4')]
    G.add_edges_from(edges)

    pos = {node: (0, i * -1) for i, node in enumerate(movies)}
    pos.update({node: (1, i * -1.5) for i, node in enumerate(casts)})

    plt.figure(figsize=(8, 5))
    nx.draw(G, pos, with_labels=True, node_size=2000,
            node_color=['skyblue' if node in movies else 'lightgreen' for node in G], edge_color='gray', font_size=10)
    plt.title("Conceptual Graph of Movies and Cast Members")
    plt.show()
