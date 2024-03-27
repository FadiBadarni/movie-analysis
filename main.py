import os

from dotenv import load_dotenv

from data_fetcher import fetch_common_cast
from neo4j_connector import Neo4jConnection
from visualization import visualize_common_cast_graph


def main():
    load_dotenv()
    neo4j_conn = Neo4jConnection(os.getenv("NEO4J_URI"), os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))

    # Fetch the total counts of movies and cast members
    # movie_count, cast_count = fetch_movies_cast_count(neo4j_conn)

    # Visualization function for movie and cast counts (to be implemented)
    # visualize_movie_cast_counts(movie_count, cast_count)

    # genre_movie_counts = fetch_genre_movie_counts(neo4j_conn)
    # visualize_genre_distribution(genre_movie_counts)

    # B = build_bipartite_graph()
    # analyze_graph(B)
    # visualize_graph(B)

    processed_data = fetch_common_cast(neo4j_conn)
    visualize_common_cast_graph(processed_data)

    neo4j_conn.close()


if __name__ == "__main__":
    main()
