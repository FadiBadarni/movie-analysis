import os

from data_process import process_movies_data
from neo4j_connector import Neo4jConnection


def fetch_movie_data():
    # Extract Neo4j credentials
    NEO4J_URI = os.getenv("NEO4J_URI")
    NEO4J_USER = os.getenv("NEO4J_USER")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

    # Initialize the Neo4j connection
    neo4j_conn = Neo4jConnection(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)

    try:
        popular_casts = fetch_popular_casts(neo4j_conn)

        movies_with_top_casts = fetch_movies_with_top_casts(neo4j_conn, popular_casts)

        return movies_with_top_casts

    except Exception as e:
        print(f"Failed to fetch data: {e}")
    finally:
        neo4j_conn.close()


def fetch_popular_casts(neo4j_conn):
    query_popular_casts = """
    MATCH (movie:Movie)-[:HAS_CAST]->(cast:Cast)
    WITH cast, COUNT(*) AS numMovies
    WHERE numMovies > 1
    RETURN cast.name AS CastName, COUNT(*) AS Appearances
    ORDER BY Appearances DESC
    LIMIT 10
    """
    result = neo4j_conn.query(query_popular_casts)
    # Convert the result into a list of cast names
    popular_casts = [record['CastName'] for record in result] if result else []
    return popular_casts


def fetch_movies_with_top_casts(neo4j_conn, popular_casts):
    placeholder_string = ', '.join([f"'{name.replace("'", "\\'")}'" for name in popular_casts])
    query_movies_with_casts = f"""
    MATCH (movie:Movie)-[:HAS_CAST]->(cast:Cast)
    WHERE cast.name IN [{placeholder_string}]
    WITH movie, cast
    ORDER BY cast.popularity DESC
    WITH movie, COLLECT(cast)[0..5] AS topCasts
    RETURN movie.title AS MovieTitle, movie.voteAverage AS VoteAverage, movie.revenue AS Revenue,
           [cast IN topCasts | cast.name] AS TopCastNames
    ORDER BY movie.releaseDate DESC
    LIMIT 5;
    """
    return neo4j_conn.query(query_movies_with_casts)


def fetch_genre_movie_counts(neo4j_conn):
    query = """
    MATCH (m:Movie)-[:HAS_GENRE]->(g:Genre)
    WITH g.name AS Genre, COUNT(m) AS MovieCount
    RETURN Genre, MovieCount ORDER BY MovieCount DESC
    """
    try:
        # Execute the query
        result = neo4j_conn.query(query)
        return result
    except Exception as e:
        print(f"Failed to fetch genre movie counts: {e}")
        return []


def fetch_common_cast(neo4j_conn):
    popular_casts = fetch_popular_casts(neo4j_conn)

    movies_data = []

    for cast_name in popular_casts:
        query = """
        MATCH (movie:Movie)-[:HAS_CAST]->(cast:Cast {name: $castName})
        RETURN movie.title AS MovieTitle, movie.releaseDate AS ReleaseDate, collect(cast.name) AS CastNames
        ORDER BY movie.releaseDate DESC
        """
        result = neo4j_conn.query(query, parameters={'castName': cast_name})
        movies_data.extend(result)

    processed_data = process_movies_data(movies_data)
    top_5_movies = processed_data[:5]

    return top_5_movies
