import os

from neo4j_connector import Neo4jConnection


def fetch_movie_data():
    # Extract Neo4j credentials
    NEO4J_URI = os.getenv("NEO4J_URI")
    NEO4J_USER = os.getenv("NEO4J_USER")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

    # Initialize the Neo4j connection
    neo4j_conn = Neo4jConnection(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)

    try:
        # Step 1: Fetch popular casts (casts with appearances in more than one movie)
        popular_casts = fetch_popular_casts(neo4j_conn)

        # Step 2: Fetch movies that feature any of these popular casts and limit to top 5 casts based on popularity
        movies_with_top_casts = fetch_movies_with_top_casts(neo4j_conn, popular_casts)

        # You can process `movies_with_top_casts` further if needed or directly return it
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
    RETURN collect(cast.name) AS popularCastNames;
    """
    result = neo4j_conn.query(query_popular_casts)
    if result:
        return result[0]['popularCastNames']
    else:
        return []


def fetch_movies_with_top_casts(neo4j_conn, popular_casts):
    # Join the cast names into a string, each name quoted and separated by commas
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
    LIMIT 25;
    """
    return neo4j_conn.query(query_movies_with_casts)

