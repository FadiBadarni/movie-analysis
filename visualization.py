import matplotlib.pyplot as plt
import networkx as nx


def visualize_graph(B):
    plt.figure(figsize=(20, 20))

    movies = [node for node, attr in B.nodes(data=True) if attr['bipartite'] == 0]
    cast = [node for node, attr in B.nodes(data=True) if attr['bipartite'] == 1]

    pos_movies = {}
    pos_cast = {}

    for index, movie in enumerate(movies):
        pos_movies[movie] = (1, -index * 2)

    for index, member in enumerate(cast):
        pos_cast[member] = (2, -index)

    pos = {**pos_movies, **pos_cast}

    nx.draw(B, pos, with_labels=True, node_size=1000,
            node_color=['skyblue' if node in movies else 'lightgreen' for node in B],
            font_size=10, alpha=0.6)

    plt.title('Bipartite Graph of Movies and Cast Members', fontsize=16)
    plt.axis('off')
    plt.show()
