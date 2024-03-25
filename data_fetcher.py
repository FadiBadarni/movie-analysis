import os

from neo4j_connector import Neo4jConnection


def fetch_movie_data():
    # Extract Neo4j credentials
    NEO4J_URI = os.getenv("NEO4J_URI")
    NEO4J_USER = os.getenv("NEO4J_USER")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

    # Initialize and use the Neo4j connection
    try:
        conn = Neo4jConnection(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)
        query = """
               MATCH (m:Movie)-[rc:HAS_CAST]->(c:Cast)
                WITH m, rc, c
                ORDER BY c.popularity DESC
                WITH m, COLLECT({cast: c, rel: rc})[0..5] AS topCastDetails
                UNWIND topCastDetails AS topCastDetail
                WITH m, topCastDetail.cast AS tc, topCastDetail.rel AS rc
                ORDER BY m.releaseDate DESC
                RETURN m.title AS movie, m.voteAverage AS voteAverage, m.revenue AS revenue,
                       COLLECT({name: tc.name, role: rc.character, popularity: tc.popularity}) AS castDetails
                LIMIT 5
        """
        results = conn.query(query)
        conn.close()
        return results
    except Exception as e:
        print(f"Failed to fetch data: {e}")
        return []

