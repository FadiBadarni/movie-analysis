import networkx as nx

from data_fetcher import fetch_movie_data


def build_bipartite_graph():
    data = fetch_movie_data()
    B = nx.Graph()

    # Add movie nodes and cast member nodes
    for record in data:
        movie_title = record["movie"]
        vote_average = record["voteAverage"]
        revenue = record["revenue"]

        # Add the movie as a node with its attributes
        B.add_node(movie_title, bipartite=0, voteAverage=vote_average, revenue=revenue)

        for cast_detail in record["castDetails"]:
            cast_name = cast_detail["name"]
            role = cast_detail["role"]
            popularity = cast_detail["popularity"]

            # Ensure each cast member is only added once
            if cast_name not in B:
                B.add_node(cast_name, bipartite=1, role=role, popularity=popularity)

            # Add edge between movie and cast member
            B.add_edge(movie_title, cast_name)

    return B
