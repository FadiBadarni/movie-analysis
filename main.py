import os

from dotenv import load_dotenv

from analysis import analyze_graph
from data_fetcher import fetch_genre_movie_counts
from graph_builder import build_bipartite_graph
from neo4j_connector import Neo4jConnection
from visualization import visualize_graph, visualize_genre_distribution


def main():
    load_dotenv()
    neo4j_conn = Neo4jConnection(os.getenv("NEO4J_URI"), os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))

    genre_movie_counts = fetch_genre_movie_counts(neo4j_conn)
    visualize_genre_distribution(genre_movie_counts)

    ##B = build_bipartite_graph()
    ##analyze_graph(B)
    ##visualize_graph(B)

    neo4j_conn.close()


if __name__ == "__main__":
    main()
