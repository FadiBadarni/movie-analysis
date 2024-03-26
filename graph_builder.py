import networkx as nx

from data_fetcher import fetch_movie_data


def build_bipartite_graph():
    data = fetch_movie_data()
    B = nx.Graph()

    # Iterate over each record from the query results
    for record in data:
        # Use dictionary key access instead of attribute access
        movie_title = record['MovieTitle']
        vote_average = record['VoteAverage']
        revenue = record['Revenue']
        top_cast_names = record['TopCastNames']  # List of top cast names

        # Add the movie as a node with its attributes
        B.add_node(movie_title, bipartite=0, voteAverage=vote_average, revenue=revenue)

        # Iterate over each cast name in the top casts for this movie
        for cast_name in top_cast_names:
            # Add the cast member node with its attribute.
            B.add_node(cast_name, bipartite=1, name=cast_name)

            # Add an edge between the movie and the cast member
            B.add_edge(movie_title, cast_name)

    return B
