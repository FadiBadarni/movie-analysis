from analysis import analyze_graph
from graph_builder import build_bipartite_graph
from visualization import visualize_graph


def main():
    B = build_bipartite_graph()
    analyze_graph(B)
    visualize_graph(B)


if __name__ == "__main__":
    main()
