import networkx as nx
import pandas as pd

from data_fetcher import fetch_movie_data


def build_bipartite_graph():
    data = fetch_movie_data()
    df = pd.DataFrame([{"movie": record["movie"], "people": record["cast"] + record["crew"]} for record in data])

    B = nx.Graph()
    B.add_nodes_from(df['movie'], bipartite=0)  # Movies
    for people in df['people']:
        B.add_nodes_from(people, bipartite=1)  # Cast/Crew

    for index, row in df.iterrows():
        movie = row['movie']
        for person in row['people']:
            B.add_edge(movie, person)

    return B
