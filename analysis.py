import networkx as nx


def analyze_graph(B):
    if B.number_of_nodes() == 0:
        print("The graph is empty.")
        return

    print("Is connected:", nx.is_bipartite(B))
    print("Number of nodes:", B.number_of_nodes())
    print("Number of edges:", B.number_of_edges())
